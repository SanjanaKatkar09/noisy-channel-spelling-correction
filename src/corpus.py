import re
from collections import Counter


def load_corpus(file_path):
    """Load the corpus from a text file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def tokenize(text):
    """Convert text into lowercase word tokens."""
    return re.findall(r"\b[a-zA-Z]+\b", text.lower())


def calculate_word_frequencies(tokens):
    """Calculate frequency of each word."""
    return Counter(tokens)


def calculate_word_probabilities(word_frequencies):
    """Calculate P(word) using corpus frequency."""
    total_words = sum(word_frequencies.values())

    probabilities = {
        word: frequency / total_words
        for word, frequency in word_frequencies.items()
    }

    return probabilities


def build_language_model(file_path):
    """Build vocabulary, frequencies and probabilities."""
    text = load_corpus(file_path)
    tokens = tokenize(text)

    frequencies = calculate_word_frequencies(tokens)
    probabilities = calculate_word_probabilities(frequencies)

    return tokens, frequencies, probabilities


if __name__ == "__main__":
    corpus_path = "data/corpus.txt"

    tokens, frequencies, probabilities = build_language_model(corpus_path)

    print("Total words:", len(tokens))
    print("Vocabulary size:", len(frequencies))

    print("\nTop 20 most frequent words:")
    for word, count in frequencies.most_common(20):
        print(f"{word:15} {count}")

    print("\nExample word probabilities:")

    for word in ["algorithm", "trained", "amount", "documents",
                 "achieved", "accuracy"]:

        print(f"P({word}) = {probabilities.get(word, 0):.6f}")