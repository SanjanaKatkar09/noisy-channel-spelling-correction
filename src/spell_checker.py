from spellchecker import SpellChecker


def correct_word(word):
    """
    Correct a single word using PySpellChecker.
    """

    spell = SpellChecker()

    correction = spell.correction(word)

    return correction


def correct_text(text):
    """
    Correct spelling errors in a complete text.
    """

    spell = SpellChecker()

    words = text.split()
    corrected_words = []

    for word in words:

        # Separate punctuation from the word
        clean_word = word.strip(".,!?;:")

        if not clean_word:
            corrected_words.append(word)
            continue

        correction = spell.correction(clean_word)

        # Preserve punctuation
        punctuation = word[len(clean_word):]

        corrected_words.append(
            correction + punctuation
        )

    return " ".join(corrected_words)


if __name__ == "__main__":

    test_words = [
        "algoritm",
        "trainned",
        "ammount",
        "documants",
        "acheived",
        "accurracy"
    ]

    print("=" * 60)
    print("STANDARD SPELL CHECKER")
    print("=" * 60)

    for word in test_words:

        correction = correct_word(word)

        print(
            f"{word:15} → {correction}"
        )

    print("\nComplete sentence:")

    text = (
        "The algoritm was trainned on a large ammount "
        "of documants and acheived good accurracy."
    )

    print("\nOriginal:")
    print(text)

    print("\nCorrected:")
    print(correct_text(text))