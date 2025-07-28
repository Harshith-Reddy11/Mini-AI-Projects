from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_text(text, num_sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return " ".join(str(sentence) for sentence in summary)

if __name__ == "__main__":
    print("📝 AI Text Summarizer")
    choice = input("Enter 1 to type text or 2 to load from a file: ")

    if choice == "1":
        text = input("Paste your long text: ")
    elif choice == "2":
        file_path = input("Enter file path: ")
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        print("Invalid choice.")
        exit()

    result = summarize_text(text)
    print("\n🔍 Summary:\n", result)
