from textblob import TextBlob


def analyze_text(text):
    blob = TextBlob(text)
    results = []
    for i, sentence in enumerate(blob.sentences, 1):
        polarity = sentence.sentiment.polarity
        subjectivity = sentence.sentiment.subjectivity
        sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
        results.append(
            f"Sentence {i}: \"{sentence}\"\n  Polarity: {polarity:.2f}, Subjectivity: {subjectivity:.2f}, Sentiment: {sentiment}"
        )
    overall_polarity = blob.sentiment.polarity
    overall_subjectivity = blob.sentiment.subjectivity
    overall_sentiment = "Positive" if overall_polarity > 0 else "Negative" if overall_polarity < 0 else "Neutral"
    results.append(
        f"\nOverall Analysis:\nPolarity: {overall_polarity:.2f}\nSubjectivity: {overall_subjectivity:.2f}\nOverall Sentiment: {overall_sentiment}"
    )
    return "\n".join(results)


def main():
    print("Sentiment Analysis Tool")
    print("1. Analyze text input")
    print("2. Analyze sentences from a file")
    choice = input("Choose an option (1/2): ").strip()
    if choice == "1":
        text = input("Enter a sentence or paragraph: ").strip()
        if not text:
            print("No input provided.")
            return
        result = analyze_text(text)
        print(result)
        save = input("Save results to file? (y/n): ").strip().lower()
        if save == "y":
            with open("sentiment_results.txt", "w", encoding="utf-8") as f:
                f.write(result)
            print("Results saved to sentiment_results.txt")
    elif choice == "2":
        filename = input("Enter filename: ").strip()
        try:
            with open(filename, "r", encoding="utf-8") as f:
                text = f.read()
            result = analyze_text(text)
            print(result)
            with open("sentiment_results.txt", "w", encoding="utf-8") as f:
                f.write(result)
            print("Results saved to sentiment_results.txt")
        except FileNotFoundError:
            print("File not found.")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
