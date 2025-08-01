# 🗣️ Speech-to-Text Converter – Mini Project  
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![License](https://img.shields.io/badge/license-MIT-green)

🎯 A simple project that captures speech from your microphone and converts it to text using Python's SpeechRecognition library.

---

## ✨ Features

- 🎤 Real-time voice input via microphone  
- 📝 Converts speech to text  
- 💾 Saves the transcription to `transcription.txt`  
- ⚠️ Handles noisy audio and errors gracefully

---

## 🛠️ Installation

Install the required libraries:

```bash
pip install SpeechRecognition
pip install pyaudio  # or sounddevice if pyaudio fails
```

---

## ▶️ Usage

1. Run the script:

```bash
python speech_to_text.py
```

2. Speak into your microphone when prompted.

3. View the output in the terminal and in `transcription.txt`.

---

## 🚧 Troubleshooting

- If you get `pyaudio` installation errors on Windows:
  - Try `pip install pipwin && pipwin install pyaudio`
  - Or use `sounddevice` as an alternative

---

## 📄 License

This project is licensed under the [MIT License](../LICENSE) and intended for educational use.

---
