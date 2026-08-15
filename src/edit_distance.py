from .corpus import build_language_model


def edit_distance(word1, word2):
    """
    Calculate the Levenshtein edit distance between two words.

    Operations:
    - Insertion
    - Deletion
    - Substitution
    """

    rows = len(word1) + 1
    cols = len(word2) + 1

    matrix = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        matrix[i][0] = i

    for j in range(cols):
        matrix[0][j] = j

    for i in range(1, rows):
        for j in range(1, cols):

            if word1[i - 1] == word2[j - 1]:
                cost = 0
            else:
                cost = 1

            matrix[i][j] = min(
                matrix[i - 1][j] + 1,
                matrix[i][j - 1] + 1,
                matrix[i - 1][j - 1] + cost
            )

    return matrix[-1][-1]


def generate_candidates(word, vocabulary, max_distance=2):
    """
    Generate candidate corrections from the corpus vocabulary.
    """

    candidates = []

    for candidate in vocabulary:

        distance = edit_distance(word, candidate)

        if distance <= max_distance:
            candidates.append((candidate, distance))

    candidates.sort(key=lambda x: x[1])

    return candidates


if __name__ == "__main__":

    # Load vocabulary from the actual corpus
    corpus_path = "data/corpus.txt"

    tokens, frequencies, probabilities = build_language_model(corpus_path)

    vocabulary = set(frequencies.keys())

    test_words = [
        "algoritm",
        "trainned",
        "ammount",
        "documants",
        "acheived",
        "accurracy"
    ]

    print("Vocabulary size:", len(vocabulary))

    for word in test_words:

        print(f"\nMisspelled word: {word}")
        print("Candidates:")

        candidates = generate_candidates(
            word,
            vocabulary,
            max_distance=2
        )

        for candidate, distance in candidates[:10]:
            print(
                f"  {candidate:15} distance = {distance}"
            )