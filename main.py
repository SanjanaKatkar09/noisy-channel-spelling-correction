import re

from src.corpus import build_language_model
from src.noisy_channel import correct_word


def correct_text(text, vocabulary, probabilities):
    """
    Correct spelling errors in a complete text.
    """

    def replace_word(match):
        word = match.group(0)
        lower_word = word.lower()

        # Keep correctly spelled words unchanged
        if lower_word in vocabulary:
            return word

        best, ranked = correct_word(
            lower_word,
            vocabulary,
            probabilities
        )

        if best:
            corrected = best[0]

            # Preserve capitalization
            if word[0].isupper():
                corrected = corrected.capitalize()

            return corrected

        return word

    corrected_text = re.sub(
        r"\b[a-zA-Z]+\b",
        replace_word,
        text
    )

    return corrected_text


def main():

    corpus_path = "data/corpus.txt"

    # Build language model
    tokens, frequencies, probabilities = build_language_model(
        corpus_path
    )

    vocabulary = set(frequencies.keys())

    noisy_text = (
        "The algoritm was trainned on a large ammount "
        "of documants and acheived good accurracy."
    )

    corrected_text = correct_text(
        noisy_text,
        vocabulary,
        probabilities
    )

    print("=" * 70)
    print("NOISY CHANNEL SPELLING CORRECTION SYSTEM")
    print("=" * 70)

    print("\nOriginal Text:")
    print(noisy_text)

    print("\nCorrected Text:")
    print(corrected_text)

    print("\n" + "=" * 70)

    # Save the result to a file
    output_path = "outputs/corrected_text.txt"

    with open(output_path, "w", encoding="utf-8") as file:
        file.write("Original Text:\n")
        file.write(noisy_text + "\n\n")
        file.write("Corrected Text:\n")
        file.write(corrected_text + "\n")

    print(f"Output saved to: {output_path}")


if __name__ == "__main__":
    main()