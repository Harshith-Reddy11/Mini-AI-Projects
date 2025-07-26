from langdetect import detect

LANGUAGES = {
    "en": "English",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "it": "Italian",
    "pt": "Portuguese",
    "ru": "Russian",
    "zh-cn": "Chinese (Simplified)",
    "zh-tw": "Chinese (Traditional)",
    "ja": "Japanese",
    "ko": "Korean",
    "ar": "Arabic",
    "hi": "Hindi",
    "bn": "Bengali",
    "tr": "Turkish",
    "nl": "Dutch",
    "pl": "Polish",
    "sv": "Swedish",
    "fi": "Finnish",
    "no": "Norwegian",
    "da": "Danish",
    "el": "Greek",
    "he": "Hebrew",
    "fa": "Persian",
    "id": "Indonesian",
    "vi": "Vietnamese",
    "th": "Thai",
    "uk": "Ukrainian",
    "ro": "Romanian",
    "hu": "Hungarian",
    "cs": "Czech",
    "sk": "Slovak",
    "sr": "Serbian",
    "hr": "Croatian",
    "bg": "Bulgarian",
    "lt": "Lithuanian",
    "lv": "Latvian",
    "et": "Estonian",
    # Add more as needed
}


def detect_language(text):
    if not text.strip():
        print("No input provided. Please enter valid text.")
        return
    try:
        lang = detect(text)
        lang_name = LANGUAGES.get(lang, "Unknown")
        print(f"Detected Language Code: {lang} ({lang_name})")
    except Exception as e:
        print(f"Could not detect the language. Error: {e}")


if __name__ == "__main__":
    print("🌐 Language Detector")
    choice = input("Enter 1 to type text or 2 to load from a file: ")

    if choice == "1":
        user_input = input("Enter your text: ")
        detect_language(user_input)

    elif choice == "2":
        file_path = input("Enter path to .txt file: ")
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                detect_language(content)
        except FileNotFoundError:
            print("File not found.")

    else:
        print("Invalid choice.")
