# 🧠 Text Summarizer – Mini Project  
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![License](https://img.shields.io/badge/license-MIT-green)

🎯 A simple NLP-powered project that automatically summarizes long text into key sentences using the LSA (Latent Semantic Analysis) algorithm. Useful for summarizing articles, conversations, or documents.

---

## ✨ Features

- 🔹 Summarizes long paragraphs into concise summaries
- 🔹 Accepts direct input or reads from a `.txt` file
- 🔹 Returns 3–5 key sentences using NLP
- 🔹 Fast and beginner-friendly with `sumy` library

---

## 🛠️ Requirements

Install the required libraries:

```bash
pip install sumy numpy
```

---

## ▶️ Usage

1. **Run the script:**

```bash
python summarizer.py
```

2. **Choose an input method:**
   - `1` → Paste long text directly
   - `2` → Read from a `.txt` file

3. **View the summary output in the terminal.**

---

## 📄 Example Input

```
Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn. 
These machines can perform tasks that typically require human intelligence, such as visual perception, speech recognition, decision-making, and language translation. 
AI is a rapidly evolving field with applications across various industries including healthcare, finance, education, and transportation. 
With advancements in machine learning and deep learning, AI systems have become more powerful and capable. 
However, concerns regarding ethics, job displacement, and data privacy continue to surround AI adoption.
```

---

## 📤 Output Example

```
🔍 Summary:
Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn. 
AI is a rapidly evolving field with applications across various industries including healthcare, finance, education, and transportation. 
However, concerns regarding ethics, job displacement, and data privacy continue to surround AI adoption.
```

---

## 🤝 Contributing

Pull requests are welcome! Feel free to fork the repo and submit improvements or new summarization models.

---

## 📄 License

This project is licensed under the [MIT License](../LICENSE) and built for educational purposes.

---
