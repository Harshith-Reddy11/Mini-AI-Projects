# 🎤 Speech-to-Text Python Project

A robust and interactive speech-to-text tool built with Python.  
Transcribe audio from your microphone or audio files, choose your language, get confidence scores, see ambient noise feedback, and save your results—all in one script!

---

## ✨ Features

- 🎙️ Transcribe speech from microphone or audio files (WAV/FLAC)
- 🌐 Supports multiple languages (English, Hindi, Telugu, French, and more)
- 🔔 Plays a beep sound before listening for speech
- 🔊 Displays detected ambient noise energy before recording
- ⭐ Shows confidence score (if available)
- 💾 Optionally save transcriptions to a file
- 🔄 Multiple attempts without restarting the script
- 🛡️ Handles errors and provides detailed feedback

---

## 🛠 Requirements

- Python 3.x  
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)

Install dependencies with:
```
pip install SpeechRecognition
```

> **Note:**  
> This script uses the built-in `winsound` module for beep sounds (Windows only).  
> For microphone input, you may also need to install [PyAudio](https://pypi.org/project/PyAudio/):
> ```
> pip install pyaudio
> ```
> If you have trouble installing PyAudio, see [PyAudio installation help](https://people.csail.mit.edu/hubert/pyaudio/#downloads).

---

## 🚀 Usage

1. **Run the script:**
   ```
   python speech_to_text.py
   ```

2. **Choose your language:**  
   Select from the displayed language codes (e.g., `en-US` for English, `hi-IN` for Hindi).

3. **Choose input method:**  
   - `1` for microphone input (speak after the beep; noise level will be shown)
   - `2` for audio file input (enter the path to a WAV/FLAC file)
   - `3` to change language
   - `4` to exit

4. **View and save results:**  
   - The transcription, confidence score (if available), and detected ambient noise energy are shown in the terminal.
   - You can save the result to `transcription.txt`.

5. **Repeat or exit:**  
   - Choose to transcribe again or exit the tool.

---

## 🌍 Supported Languages

- English (US/India)
- Hindi
- Telugu
- French
- Spanish
- German
- Chinese (Mandarin)
- *(Add more as needed in the `LANGUAGES` dictionary)*

---

## 📜 License

This project is for educational and personal use.

