import cv2
import random
import streamlit as st
from deepface import DeepFace
import numpy as np
from PIL import Image

# 🎵 Emotion-to-song mapping (English + Hindi + Punjabi)
emotion_songs = {
    "happy": {
        # English
        "Pharrell Williams - Happy": "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
        "Ed Sheeran - Shape of You": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
        "Mark Ronson ft. Bruno Mars - Uptown Funk": "https://www.youtube.com/watch?v=OPf0YbXqDm0",
        "Katrina & The Waves - Walking on Sunshine": "https://www.youtube.com/watch?v=iPUmE-tne5U",
        # Hindi
        "A.R. Rahman - Jai Ho": "https://www.youtube.com/watch?v=5k1hSu2gdKE",
        "Katrina Kaif - Swag Se Swagat": "https://www.youtube.com/watch?v=xmU0s2QtaEY",
        "Gallan Goodiyan - Dil Dhadakne Do": "https://www.youtube.com/watch?v=q2d8J9gmnG0",
        "Badtameez Dil - Yeh Jawaani Hai Deewani": "https://www.youtube.com/watch?v=II2EO3Nw4m0",
        # Punjabi
        "Diljit Dosanjh - Lover": "https://www.youtube.com/watch?v=5eTzRrZCdn4",
        "AP Dhillon - Brown Munde": "https://www.youtube.com/watch?v=HD3gjeZzJ9w",
        "Jass Manak - Lehanga": "https://www.youtube.com/watch?v=J8J9hH8bH3M",
        "Amrit Maan - Trending Nakhra": "https://www.youtube.com/watch?v=HMyCGKc2Qh4"
    },
    "sad": {
        # English
        "Adele - Someone Like You": "https://www.youtube.com/watch?v=hLQl3WQQoQ0",
        "Sam Smith - Stay With Me": "https://www.youtube.com/watch?v=pB-5XG-DbAA",
        "Coldplay - Fix You": "https://www.youtube.com/watch?v=k4V3Mo61fJM",
        "Lewis Capaldi - Someone You Loved": "https://www.youtube.com/watch?v=zABLecsR5UE",
        # Hindi
        "Arijit Singh - Channa Mereya": "https://www.youtube.com/watch?v=284Ov7ysmfA",
        "Kabira - Yeh Jawaani Hai Deewani": "https://www.youtube.com/watch?v=jHNNMj5bNQw",
        "Tum Hi Ho - Aashiqui 2": "https://www.youtube.com/watch?v=Umqb9KENgmk",
        "Jeene Laga Hoon - Ramaiya Vastavaiya": "https://www.youtube.com/watch?v=vfNQw4ptt4w",
        # Punjabi
        "Amrinder Gill - Supna": "https://www.youtube.com/watch?v=O2uT-LwFGOo",
        "Sidhu Moose Wala - 295": "https://www.youtube.com/watch?v=VXmsqU5zD7I",
        "B Praak - Filhall": "https://www.youtube.com/watch?v=0J9lqWFMHkY",
        "Ranjit Bawa - Yaari Chandigarh Waliye": "https://www.youtube.com/watch?v=t6eRkfpF6Tw"
    },
    "angry": {
        # English
        "Eminem - Till I Collapse": "https://www.youtube.com/watch?v=ytQ5CYE1VZw",
        "Linkin Park - Numb": "https://www.youtube.com/watch?v=kXYiU_JCYtU",
        "Metallica - Enter Sandman": "https://www.youtube.com/watch?v=CD-E-LDc384",
        "Rage Against The Machine - Killing in the Name": "https://www.youtube.com/watch?v=bWXazVhlyxQ",
        # Hindi
        "Malhari - Bajirao Mastani": "https://www.youtube.com/watch?v=O1oGJZ3ycvc",
        "Zinda - Bhaag Milkha Bhaag": "https://www.youtube.com/watch?v=vnXjV_fV-fA",
        "Sultan Title Track": "https://www.youtube.com/watch?v=wPxqcq6Byq0",
        "Sher Aaya Sher - Gully Boy": "https://www.youtube.com/watch?v=4s10jK3BDTk",
        # Punjabi
        "Sidhu Moose Wala - Same Beef": "https://www.youtube.com/watch?v=QJ5jSHiA6sg",
        "Karan Aujla - Don't Look": "https://www.youtube.com/watch?v=6aAnXGzVfOQ",
        "Amrit Maan - Guerrilla War": "https://www.youtube.com/watch?v=PMrbY2fmpoY",
        "Shubh - We Rollin": "https://www.youtube.com/watch?v=90TLyaYagRA"
    },
    "neutral": {
        # English
        "Ed Sheeran - Perfect": "https://www.youtube.com/watch?v=2Vv-BfVoq4g",
        "Coldplay - The Scientist": "https://www.youtube.com/watch?v=3JZ4pnNtyxQ",
        "John Mayer - Gravity": "https://www.youtube.com/watch?v=Fo4746ZYLQ0",
        "Norah Jones - Don't Know Why": "https://www.youtube.com/watch?v=tO4dxvguQDk",
        # Hindi
        "Phir Le Aaya Dil - Barfi": "https://www.youtube.com/watch?v=4LxlHOZ6_N8",
        "Tera Ban Jaunga - Kabir Singh": "https://www.youtube.com/watch?v=0HdC-AYcldw",
        "Pee Loon - Once Upon a Time in Mumbaai": "https://www.youtube.com/watch?v=xH1zV0R2nq8",
        "Kaun Tujhe - M.S. Dhoni": "https://www.youtube.com/watch?v=LF3fiDUZ7po",
        # Punjabi
        "Mann Bharrya - B Praak": "https://www.youtube.com/watch?v=18oKzJSSMS8",
        "Jannat - B Praak": "https://www.youtube.com/watch?v=3nFx0zHmiDg",
        "Qismat - Ammy Virk": "https://www.youtube.com/watch?v=uJc7H6yqf_g",
        "Sakhiyaan - Maninder Buttar": "https://www.youtube.com/watch?v=9Ckhd0ee4YA"
    },
    "surprise": {
        # English
        "Queen - Bohemian Rhapsody": "https://www.youtube.com/watch?v=fJ9rUzIMcZQ",
        "Imagine Dragons - Thunder": "https://www.youtube.com/watch?v=fKopy74weus",
        "Michael Jackson - Smooth Criminal": "https://www.youtube.com/watch?v=h_D3VFfhvs4",
        "Gotye - Somebody That I Used to Know": "https://www.youtube.com/watch?v=8UVNT4wvIGY",
        # Hindi
        "Kala Chashma - Baar Baar Dekho": "https://www.youtube.com/watch?v=k4yXQkG2s1E",
        "Nashe Si Chadh Gayi - Befikre": "https://www.youtube.com/watch?v=PQmrmVs10X8",
        "London Thumakda - Queen": "https://www.youtube.com/watch?v=olNwA9eG9s8",
        "Dil Dhadakne Do - Zindagi Na Milegi Dobara": "https://www.youtube.com/watch?v=cWIeYj9kHg8",
        # Punjabi
        "3 Peg - Sharry Mann": "https://www.youtube.com/watch?v=Vhdpumv4n1w",
        "Laung Laachi - Mannat Noor": "https://www.youtube.com/watch?v=2vYq3DaFz2I",
        "Morni Banke - Guru Randhawa": "https://www.youtube.com/watch?v=nTjrvJQDeJw",
        "Patiala Peg - Diljit Dosanjh": "https://www.youtube.com/watch?v=VhkG3w2hZrk"
    },
    "fear": {
        # English
        "Michael Jackson - Thriller": "https://www.youtube.com/watch?v=sOnqjkJTMaA",
        "Evanescence - Bring Me to Life": "https://www.youtube.com/watch?v=3YxaaGgTQYM",
        "Linkin Park - In the End": "https://www.youtube.com/watch?v=eVTXPUF4Oz4",
        "AC/DC - Highway to Hell": "https://www.youtube.com/watch?v=l482T0yNkeo",
        # Hindi
        "Bhoot Title Track": "https://www.youtube.com/watch?v=3gGeNP89WSk",
        "Jadoo Hai Nasha Hai - Jism": "https://www.youtube.com/watch?v=8G9M4BR7XCM",
        "Tujhe Bhula Diya - Anjaana Anjaani": "https://www.youtube.com/watch?v=yU6d06sG5Vw",
        "Aakhon Mein Teri - Om Shanti Om": "https://www.youtube.com/watch?v=Pr7vv2eFqkA",
        # Punjabi
        "Bewafa - Imran Khan": "https://www.youtube.com/watch?v=j5-yKhDd64s",
        "Yaad - Tegi Pannu": "https://www.youtube.com/watch?v=kZxjE_TyhjM",
        "Pachtaoge - Arijit Singh": "https://www.youtube.com/watch?v=4t6r1uKkZpA",
        "Hathyar - Sidhu Moose Wala": "https://www.youtube.com/watch?v=0-5Wjpp8Hb0"
    }
}

# Streamlit UI Config
st.set_page_config(page_title="🎭 Emotion-Based Song Recommender", layout="centered")
st.title("🎭 Emotion-Based Song Recommender 🎵")
st.markdown("📸 Capture an image to analyze your emotion and get **multiple song recommendations**!")

# Camera input
img_file_buffer = st.camera_input("Take a Picture")

if img_file_buffer:
    try:
        img = Image.open(img_file_buffer)
        img_array = np.array(img)

        st.info("🔍 Analyzing emotion, please wait...")
        analysis = DeepFace.analyze(
            img_array,
            actions=['emotion'],
            enforce_detection=False,
            detector_backend="opencv"
        )

        detected_emotion = analysis[0]['dominant_emotion'].lower()
        st.success(f"🎯 Detected Emotion: **{detected_emotion.capitalize()}**")

        if detected_emotion in emotion_songs:
            all_songs = list(emotion_songs[detected_emotion].items())
            random_songs = random.sample(all_songs, min(5, len(all_songs)))  # Pick 5 songs

            st.subheader("🎶 Recommended Songs for You:")
            for song_name, song_link in random_songs:
                st.markdown(f"**{song_name}**")
                youtube_id = song_link.split("v=")[-1]
                st.video(f"https://www.youtube.com/embed/{youtube_id}")

        else:
            st.warning("No matching songs found for this emotion.")

    except Exception as e:
        st.error("❌ Could not detect emotion. Please try again.")
        st.code(str(e))
