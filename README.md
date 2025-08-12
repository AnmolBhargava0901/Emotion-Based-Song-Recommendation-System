
# 🎭 Emotion-Based Song Recommender 🎵


![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![DeepFace](https://img.shields.io/badge/DeepFace-Emotion%20Detection-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Overview

The **Emotion-Based Song Recommender** uses **AI-powered emotion detection** from your webcam to recommend **personalized songs** in **English, Hindi, and Punjabi**.
Whether you're happy, sad, or ready to rage — we’ve got a playlist for every mood!

💡 *Just take a selfie and let the app handle the rest.*

---

## ✨ Features

* 📸 **Live Emotion Detection** — Uses **DeepFace** to analyze facial expressions.
* 🎶 **Multi-Language Songs** — Curated in **English, Hindi & Punjabi**.
* 🤖 **AI-Powered Matching** — Matches your mood to the best songs.
* 🎥 **Embedded YouTube Player** — Play songs without leaving the app.
* 🎨 **Clean Streamlit UI** — Fully interactive and responsive.

---

## 📷 Supported Emotions & Song Count

| Emotion  | English | Hindi | Punjabi | Total |
| -------- | ------- | ----- | ------- | ----- |
| Happy    | 4       | 4     | 4       | 12    |
| Sad      | 4       | 4     | 4       | 12    |
| Angry    | 4       | 4     | 4       | 12    |
| Neutral  | 4       | 4     | 4       | 12    |
| Surprise | 4       | 4     | 4       | 12    |
| Fear     | 4       | 4     | 4       | 12    |

---

## 🛠️ Tech Stack

* **[Python](https://www.python.org/)** — Core programming language
* **[Streamlit](https://streamlit.io/)** — Web app framework
* **[DeepFace](https://github.com/serengil/deepface)** — Facial emotion detection
* **[OpenCV](https://opencv.org/)** — Image processing
* **[Pillow](https://python-pillow.org/)** — Image handling
* **NumPy** — Array and image manipulation

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/emotion-song-recommender.git
cd emotion-song-recommender
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
emotion-song-recommender/
│
├── app.py                # Main application script
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── assets/               # Images & icons (optional)
```

---

## 📸 How It Works

1. **Take a Picture** using your webcam in the app.
2. **DeepFace** analyzes your facial expression to detect emotion.
3. **AI Song Selector** picks **5 random songs** from your emotion category.
4. 🎧 Enjoy listening — right inside the app!



Would you like me to also make a **beautiful banner image** for this README so it instantly stands out on GitHub? That would make it way more attractive.
