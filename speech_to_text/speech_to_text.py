# speech_to_text.py

import speech_recognition as sr

def transcribe_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("🎙️ Speak now... (Press Ctrl+C to stop)")
    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        print("🔍 Transcribing...")
        text = recognizer.recognize_google(audio)
        print("\n📝 Transcription:\n", text)

        # Optionally save the text
        with open("transcription.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("\n✅ Transcription saved to transcription.txt")

    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
    except sr.RequestError:
        print("❌ Could not request results from the speech recognition service.")
    except KeyboardInterrupt:
        print("\n🛑 Stopped manually.")

if __name__ == "__main__":
    transcribe_speech()
