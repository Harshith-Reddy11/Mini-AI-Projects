🎯 A beginner-friendly Python project that performs sentiment analysis using natural language processing. Ideal for text analysis tasks like customer feedback, reviews, or social media posts.


# 💬 Sentiment Analysis – Mini Project

This is a simple Python project that analyzes the **sentiment of text** using [TextBlob](https://textblob.readthedocs.io/en/dev/). It can process direct user input or read sentences from a text file, providing **polarity**, **subjectivity**, and **sentiment classification** for each sentence and the overall text.

---

## ✨ Features

- 🔍 Analyze sentiment for each sentence and the entire text  
- 📊 Displays polarity and subjectivity scores  
- ✅ Classifies sentiment as Positive, Negative, or Neutral  
- 📂 Supports input from the user or a `.txt` file  
- 💾 Optionally saves results to `sentiment_results.txt`

---

## 🛠️ Requirements

- 🐍 Python 3.x  
- 📦 [TextBlob](https://pypi.org/project/textblob/)

Install with:

```bash
pip install textblob
```

(Optional for best results):

```bash
python -m textblob.download_corpora
```

---

## ▶️ Usage

1. **Run the script:**

   ```bash
   python sentiment_analysis.py
   ```

2. **Choose an option:**
   - `1` → Analyze direct text input  
   - `2` → Analyze sentences from a file

3. **For file analysis:**
   - Place your `.txt` file (e.g., `input.txt`) in the same folder as the script, or provide the full path when prompted

4. **View results:**
   - 🖥️ Printed in the terminal  
   - 💾 Optionally saved to `sentiment_results.txt`

---

## 📄 Example Input File (`input.txt`)

```
I love sunny days. The weather is perfect for a walk in the park.
However, sometimes it gets too hot and uncomfortable.
Overall, I enjoy spending time outdoors.
Rainy days make me feel a bit gloomy, but I appreciate the freshness they bring.
```

---

## 📄 License

This project is for **educational purposes** only.

---
