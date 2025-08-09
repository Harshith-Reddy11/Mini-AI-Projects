# 📝 AI TEXT SUMMARIZER

A beginner-friendly Python project that summarizes long text using natural language processing.  
Choose from multiple algorithms and customize the summary length. Great for condensing articles, reports, or any lengthy content!

---

## ✨ Features

- 📚 Summarizes text from direct input or a file
- ⚡ Choose summarization algorithm: LSA, LexRank, or Luhn
- 📝 Customizable number of sentences in the summary
- 💾 Optionally save the summary to `summary.txt`
- 🚫 Handles empty input and file errors gracefully

---

## 🛠 Requirements

- 🐍 Python 3.x  
- [sumy](https://pypi.org/project/sumy/)

Install with:
```
pip install sumy
```

---

## 🚀 Usage

1. **Run the script:**
   ```
   python summarizer.py
   ```

2. **Choose an option:**
   - Enter `1` to paste text directly
   - Enter `2` to load text from a file

3. **Customize:**
   - Enter the number of sentences for the summary (default is 3)
   - Choose the algorithm: `lsa`, `lexrank`, or `luhn` (default is `lsa`)

4. **View and save results:**
   - The summary is displayed in the terminal
   - Optionally save it to `summary.txt`

---

## 📄 Example

**Direct input:**
```
Enter 1 to type text or 2 to load from a file: 1
Paste your long text: Artificial intelligence is transforming the world...
How many sentences in the summary? (default 3): 2
Choose algorithm: lsa / lexrank / luhn (default lsa): luhn

🔍 Summary:
Artificial intelligence is transforming the world... [summary output]
```

**File input:**
```
Enter 1 to type text or 2 to load from a file: 2
Enter file path: article.txt
How many sentences in the summary? (default 3): 
Choose algorithm: lsa / lexrank / luhn (default lsa): 
```

---

## 📜 License

This project is licensed under the [MIT License](../LICENSE) and intended for **educational use**.

---


