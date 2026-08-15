import matplotlib.pyplot as plt


def create_comparison_graph():
    metrics = ["Precision", "Recall", "F1-Score"]

    noisy_channel = [95.83, 95.83, 95.83]
    spell_checker = [100.00, 100.00, 100.00]

    x = range(len(metrics))

    width = 0.35

    plt.figure(figsize=(8, 5))

    plt.bar(
        [i - width / 2 for i in x],
        noisy_channel,
        width=width,
        label="Noisy Channel"
    )

    plt.bar(
        [i + width / 2 for i in x],
        spell_checker,
        width=width,
        label="Standard Spell Checker"
    )

    plt.xlabel("Evaluation Metrics")
    plt.ylabel("Score (%)")
    plt.title("Spelling Correction Performance Comparison")

    plt.xticks(list(x), metrics)
    plt.ylim(0, 110)

    plt.legend()

    plt.tight_layout()

    output_path = "outputs/performance_comparison.png"

    plt.savefig(output_path, dpi=300)

    print(f"Graph saved to: {output_path}")


if __name__ == "__main__":
    create_comparison_graph()