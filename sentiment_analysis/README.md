# Sentiment Analysis Mini Project

This is a simple Python project that analyzes the sentiment of text using [TextBlob](https://textblob.readthedocs.io/en/dev/). It can process direct user input or read sentences from a text file, providing polarity, subjectivity, and sentiment classification for each sentence and overall text.

## Features

- Analyze sentiment for each sentence and overall text
- Displays polarity and subjectivity scores
- Classifies sentiment as Positive, Negative, or Neutral
- Supports input from the user or a text file
- Optionally saves results to `sentiment_results.txt`

## Requirements

- Python 3.x
- [TextBlob](https://pypi.org/project/textblob/)

Install TextBlob with:
```
pip install textblob
```

## Usage

1. **Run the script:**
   ```
   python sentiment_analysis.py
   ```

2. **Choose an option:**
   - `1` to analyze direct text input
   - `2` to analyze sentences from a file

3. **For file analysis:**
   - Place your `.txt` file (e.g., `input.txt`) in the same folder as the script, or provide the full path when prompted.

4. **View results:**
   - Results are printed in the terminal and can be saved to `sentiment_results.txt`.

## Example Input File

```
I love sunny days. The weather is perfect for a walk in the park.
However, sometimes it gets too hot and uncomfortable.
Overall, I enjoy spending time outdoors.
Rainy days make me feel a bit gloomy, but I appreciate the freshness they bring.
```

## License

This project is for educational purposes.
