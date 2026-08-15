from .corpus import build_language_model
from .edit_distance import generate_candidates, edit_distance

def error_probability(misspelled_word, candidate_word):
    """
    Estimate the probability of observing a spelling error.

    Smaller edit distance means a more likely correction.
    """

    distance = edit_distance(misspelled_word, candidate_word)

    return 1 / (1 + distance)


def noisy_channel_score(
    misspelled_word,
    candidate_word,
    word_probability
):
    """
    Calculate the Noisy Channel score.

    Score = P(candidate) * P(error | candidate)
    """

    error_prob = error_probability(
        misspelled_word,
        candidate_word
    )

    return word_probability * error_prob


def correct_word(
    misspelled_word,
    vocabulary,
    probabilities,
    max_distance=2
):
    """
    Find the best correction using the Noisy Channel Model.
    """

    candidates = generate_candidates(
        misspelled_word,
        vocabulary,
        max_distance
    )

    ranked_candidates = []

    for candidate, distance in candidates:

        probability = probabilities.get(candidate, 0)

        score = noisy_channel_score(
            misspelled_word,
            candidate,
            probability
        )

        ranked_candidates.append(
            (candidate, distance, probability, score)
        )

    # Highest score first
    ranked_candidates.sort(
        key=lambda x: x[3],
        reverse=True
    )

    if ranked_candidates:
        return ranked_candidates[0], ranked_candidates

    return None, []


if __name__ == "__main__":

    corpus_path = "data/corpus.txt"

    # Build language model
    tokens, frequencies, probabilities = build_language_model(
        corpus_path
    )

    vocabulary = set(frequencies.keys())

    test_words = [
        "algoritm",
        "trainned",
        "ammount",
        "documants",
        "acheived",
        "accurracy"
    ]

    print("=" * 60)
    print("NOISY CHANNEL SPELLING CORRECTION")
    print("=" * 60)

    for word in test_words:

        best, ranked = correct_word(
            word,
            vocabulary,
            probabilities
        )

        print(f"\nMisspelled word: {word}")

        print("\nRanked candidates:")

        for candidate, distance, probability, score in ranked[:5]:

            print(
                f"{candidate:15}"
                f" distance={distance}"
                f" P(word)={probability:.6f}"
                f" score={score:.8f}"
            )

        if best:
            print(f"\nBest correction: {best[0]}")