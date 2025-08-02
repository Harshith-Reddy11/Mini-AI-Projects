# speech_to_text.py

import speech_recognition as sr
import winsound
import os

LANGUAGES = {
    "en-US": "English (US)",
    "en-IN": "English (India)",
    "hi-IN": "Hindi",
    "te-IN": "Telugu",
    "fr-FR": "French",
    "es-ES": "Spanish",
    "de-DE": "German",
    "zh-CN": "Chinese (Mandarin)",
    # Add more as needed
}


def choose_language():
    print("\n🌐 Available Languages:")
    for code, name in LANGUAGES.items():
        print(f"{code}: {name}")
    lang = input("Enter language code (default en-US): ").strip()
    return lang if lang in LANGUAGES else "en-US"




def play_beep():
    try:
        winsound.Beep(1000, 300)  # frequency in Hz, duration in ms
    except Exception as e:
        print(f"🔔 (Could not play beep: {e})")


def transcribe_from_microphone(recognizer, language):
    mic = sr.Microphone()
    print("🎙️ Speak now...")
    play_beep()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    return audio


def transcribe_from_file(recognizer, language):
    file_path = input("Enter audio file path (WAV/FLAC): ").strip()
    if not os.path.exists(file_path):
        print("❌ File not found.")
        return None
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    return audio


def recognize_audio(recognizer, audio, language):
    try:
        response = recognizer.recognize_google(
            audio, language=language, show_all=True)
        if not response or "alternative" not in response:
            print("❌ No transcription could be made.")
            return None
        best = response["alternative"][0]
        text = best.get("transcript", "")
        confidence = best.get("confidence", None)
        print("\n📝 Transcription:\n", text)
        if confidence is not None:
            print(f"⭐ Confidence: {confidence*100:.2f}%")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
    except sr.RequestError as e:
        print(
            f"❌ Could not request results from the speech recognition service.\nDetails: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    return None


def main():
    recognizer = sr.Recognizer()
    print("🎤 Speech-to-Text Tool")
    language = choose_language()
    while True:
        print("\nOptions:\n1. Microphone\n2. Audio File\n3. Change Language\n4. Exit")
        choice = input("Choose input method (1/2/3/4): ").strip()
        if choice == "1":
            try:
                audio = transcribe_from_microphone(recognizer, language)
            except KeyboardInterrupt:
                print("\n🛑 Stopped manually.")
                continue
        elif choice == "2":
            audio = transcribe_from_file(recognizer, language)
            if audio is None:
                continue
        elif choice == "3":
            language = choose_language()
            continue
        elif choice == "4":
            print("👋 Exiting.")
            break
        else:
            print("❌ Invalid choice.")
            continue

        text = recognize_audio(recognizer, audio, language)
        if text:
            save = input(
                "💾 Save transcription to file? (y/n): ").strip().lower()
            if save == "y":
                with open("transcription.txt", "w", encoding="utf-8") as f:
                    f.write(text)
                print("✅ Transcription saved to transcription.txt")

        again = input("\n🔄 Transcribe again? (y/n): ").strip().lower()
        if again != "y":
            print("👋 Exiting.")
            break


if __name__ == "__main__":
    main()
