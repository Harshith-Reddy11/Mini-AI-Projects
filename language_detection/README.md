# Language Detector Mini Project

This Python project detects the language of a given text using [langdetect](https://pypi.org/project/langdetect/).  
You can enter text directly or provide a `.txt` file for detection. The tool maps detected language codes to human-readable names.

## Features

- Detects language from user input or a text file
- Maps language codes to full language names
- Handles empty input and file errors gracefully
- Supports many world languages

## Requirements

- Python 3.x
- [langdetect](https://pypi.org/project/langdetect/)

Install with:
```
pip install langdetect
```

## Usage

1. **Run the script:**
   ```
   python language_detector.py
   ```

2. **Choose an option:**
   - Enter `1` to type text directly
   - Enter `2` to provide a path to a `.txt` file

3. **View results:**  
   The detected language code and name will be printed in the terminal.

## Example

**Direct input:**
```
Enter 1 to type text or 2 to load from a file: 1
Enter your text: Bonjour tout le monde!
Detected Language Code: fr (French)
```

**File input:**
```
Enter 1 to type text or 2 to load from a file: 2
Enter path to .txt file: input.txt
Detected Language Code: en (English)
```

## License

This project is for educational purposes.
