from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer


def summarize_text(text, num_sentences=3, algo="lsa"):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    if algo == "lsa":
        summarizer = LsaSummarizer()
    elif algo == "lexrank":
        summarizer = LexRankSummarizer()
    elif algo == "luhn":
        summarizer = LuhnSummarizer()
    else:
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
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
        except FileNotFoundError:
            print("File not found.")
            exit()
    else:
        print("Invalid choice.")
        exit()

    if not text.strip():
        print("No input provided.")
        exit()

    try:
        num_sentences = int(
            input("How many sentences in the summary? (default 3): ") or 3)
    except ValueError:
        num_sentences = 3

    algo = input(
        "Choose algorithm: lsa / lexrank / luhn (default lsa): ").strip().lower() or "lsa"

    result = summarize_text(text, num_sentences, algo)
    print("\n🔍 Summary:\n", result)

    save = input("Save summary to file? (y/n): ").strip().lower()
    if save == "y":
        with open("summary.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("Summary saved to summary.txt")
