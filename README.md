# Noisy Channel Spelling Correction

An NLP-based spelling correction system implemented using the **Noisy Channel Model**, **Levenshtein Edit Distance**, and corpus-based word probabilities.

## Project Overview

Spelling errors are common in text and can affect the performance of Natural Language Processing systems. This project develops a statistical spelling correction system that identifies misspelled words, generates possible corrections, and selects the most probable candidate using the Noisy Channel Model.

The system is also compared with a standard Python spell-checking library.

## Problem Statement

Given a noisy text containing spelling errors, identify the incorrect words and generate the most likely corrections using statistical language information and edit distance.

### Example

**Input:**

```text
The algoritm was trainned on a large ammount of documants and acheived good accurracy.
```

**Corrected Output:**

```text
The algorithm was trained on a large amount of documents and achieved good accuracy.
```

## Objectives

* Implement spelling correction using the Noisy Channel Model.
* Generate candidate corrections using Edit Distance.
* Estimate word probabilities from a corpus.
* Rank candidate corrections using probability and spelling similarity.
* Compare the proposed system with a standard spell checker.
* Evaluate the systems using Precision, Recall, and F1-score.

## Methodology

The system follows the pipeline:

```text
Input Text
    ↓
Tokenization
    ↓
Vocabulary Creation
    ↓
Word Frequency & Probability
    ↓
Misspelling Detection
    ↓
Edit Distance Candidate Generation
    ↓
Noisy Channel Scoring
    ↓
Best Candidate Selection
    ↓
Corrected Text
```

## Noisy Channel Model

The system uses the following scoring concept:

```text
Score(candidate | observed word)
        ∝
P(observed word | candidate) × P(candidate)
```

The candidate probability is estimated from the corpus, while edit distance is used to estimate the likelihood of the spelling error.

## Technologies Used

* Python
* Natural Language Processing
* Noisy Channel Model
* Levenshtein Edit Distance
* PySpellChecker
* Matplotlib
* CSV
* Git & GitHub

## Project Structure

```text
noisy-channel-spelling-correction/
│
├── data/
│   ├── corpus.txt
│   └── test_data.csv
│
├── src/
│   ├── __init__.py
│   ├── corpus.py
│   ├── edit_distance.py
│   ├── noisy_channel.py
│   ├── spell_checker.py
│   ├── evaluation.py
│   └── visualization.py
│
├── outputs/
│   ├── corrected_text.txt
│   ├── evaluation_results.csv
│   ├── performance_comparison.png
│   └── error_analysis.txt
│
├── notebooks/
├── screenshots/
├── report/
│
├── main.py
├── requirements.txt
└── README.md
```

## Results

The system was evaluated using 24 spelling-error test cases.

| Metric    | Noisy Channel | Standard Spell Checker |
| --------- | ------------: | ---------------------: |
| Precision |        95.83% |                100.00% |
| Recall    |        95.83% |                100.00% |
| F1-Score  |        95.83% |                100.00% |

The Noisy Channel Model correctly corrected **23 out of 24** test cases, while the standard spell checker correctly handled **24 out of 24**.

## Error Analysis

The Noisy Channel Model incorrectly handled the following case:

```text
Input:       algoritms
Expected:    algorithms
Predicted:   algorithm
```

Both `algorithm` and `algorithms` are possible candidates based on edit distance. Because the current corpus assigns a higher probability to `algorithm`, the Noisy Channel Model selects the singular form.

This demonstrates that a small corpus can limit the effectiveness of corpus-based probability estimation.

## Future Improvements

* Use a larger and more diverse corpus.
* Add character-level error probabilities.
* Incorporate sentence context using bigram or trigram probabilities.
* Improve candidate ranking using contextual information.
* Test the system on a larger spelling-error dataset.
* Add a user interface for interactive spelling correction.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/SanjanaKatkar09/noisy-channel-spelling-correction.git
cd noisy-channel-spelling-correction
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the spelling correction system

```bash
python main.py
```

### 6. Run the standard spell checker

```bash
python -m src.spell_checker
```

### 7. Run evaluation

```bash
python -m src.evaluation
```

### 8. Generate the performance graph

```bash
python -m src.visualization
```

## Author

**Sanjana Katkar09**

NLP Practical Project — Spelling Correction using Noisy Channel Model
