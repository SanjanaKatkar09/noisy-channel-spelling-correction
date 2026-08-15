import csv

from src.corpus import build_language_model
from src.noisy_channel import correct_word as noisy_channel_correct
from src.spell_checker import correct_word as spell_checker_correct


def load_test_data(file_path):
    """Load incorrect and correct word pairs from CSV."""

    test_data = []

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            test_data.append(
                (
                    row["incorrect"].strip().lower(),
                    row["correct"].strip().lower()
                )
            )

    return test_data


def evaluate_predictions(test_data, predictions):
    """
    Calculate Precision, Recall and F1-score.

    TP = correctly corrected spelling errors
    FP = incorrect corrections
    FN = spelling errors that were not corrected
    """

    true_positive = 0
    false_positive = 0
    false_negative = 0

    for (_, actual), predicted in zip(test_data, predictions):

        actual = actual.strip().lower()
        predicted = predicted.strip().lower()
        
        if predicted == actual:
            true_positive += 1
        else:
            false_positive += 1
            false_negative += 1

    if true_positive + false_positive == 0:
        precision = 0
    else:
        precision = true_positive / (
            true_positive + false_positive
        )

    if true_positive + false_negative == 0:
        recall = 0
    else:
        recall = true_positive / (
            true_positive + false_negative
        )

    if precision + recall == 0:
        f1_score = 0
    else:
        f1_score = (
            2 * precision * recall
            / (precision + recall)
        )

    return precision, recall, f1_score


def evaluate_noisy_channel(test_data):
    """Generate predictions using the Noisy Channel Model."""

    (
        tokens,
        frequencies,
        probabilities
    ) = build_language_model("data/corpus.txt")

    vocabulary = set(frequencies.keys())

    predictions = []

    for incorrect, actual in test_data:

        best, ranked = noisy_channel_correct(
            incorrect,
            vocabulary,
            probabilities
        )

        if best:
            predictions.append(best[0])
        else:
            predictions.append(incorrect)

    return predictions


def evaluate_spell_checker(test_data):
    """Generate predictions using PySpellChecker."""

    predictions = []

    for incorrect, actual in test_data:

        prediction = spell_checker_correct(incorrect)

        predictions.append(prediction)

    return predictions


def print_results(
    test_data,
    noisy_predictions,
    spell_predictions
):
    """Display word-level comparison and evaluation results."""

    print("=" * 75)
    print("SPELLING CORRECTION EVALUATION")
    print("=" * 75)

    print(
        f"\n{'Incorrect':15}"
        f"{'Actual':15}"
        f"{'Noisy Channel':20}"
        f"{'Spell Checker':20}"
    )

    print("-" * 75)

    for (incorrect, actual), noisy, spell in zip(
        test_data,
        noisy_predictions,
        spell_predictions
    ):

        print(
            f"{incorrect:15}"
            f"{actual:15}"
            f"{noisy:20}"
            f"{spell:20}"
        )

    noisy_precision, noisy_recall, noisy_f1 = (
        evaluate_predictions(
            test_data,
            noisy_predictions
        )
    )

    spell_precision, spell_recall, spell_f1 = (
        evaluate_predictions(
            test_data,
            spell_predictions
        )
    )

    print("\n" + "=" * 75)
    print("PERFORMANCE COMPARISON")
    print("=" * 75)

    print(
        f"\n{'Metric':15}"
        f"{'Noisy Channel':20}"
        f"{'Spell Checker':20}"
    )

    print("-" * 55)

    print(
        f"{'Precision':15}"
        f"{noisy_precision:.4f}"
        f"{'':14}"
        f"{spell_precision:.4f}"
    )

    print(
        f"{'Recall':15}"
        f"{noisy_recall:.4f}"
        f"{'':14}"
        f"{spell_recall:.4f}"
    )

    print(
        f"{'F1-Score':15}"
        f"{noisy_f1:.4f}"
        f"{'':14}"
        f"{spell_f1:.4f}"
    )

def save_results(
    test_data,
    noisy_predictions,
    spell_predictions,
    output_path="outputs/evaluation_results.csv"
):
    """Save detailed evaluation results to CSV."""

    with open(output_path, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Incorrect",
            "Actual",
            "Noisy_Channel",
            "Spell_Checker",
            "Noisy_Correct",
            "Spell_Correct"
        ])

        for (incorrect, actual), noisy, spell in zip(
            test_data,
            noisy_predictions,
            spell_predictions
        ):

            writer.writerow([
                incorrect,
                actual,
                noisy,
                spell,
                noisy == actual,
                spell == actual
            ])

    print(f"\nDetailed results saved to: {output_path}")


def main():

    test_file = "data/test_data.csv"

    test_data = load_test_data(test_file)

    noisy_predictions = evaluate_noisy_channel(
        test_data
    )

    spell_predictions = evaluate_spell_checker(
        test_data
    )

    print_results(
        test_data,
        noisy_predictions,
        spell_predictions
    )

    save_results(
    test_data,
    noisy_predictions,
    spell_predictions
    )


if __name__ == "__main__":
    main()