 🛠️ How to Use

1. Prepare a plain text file with one sequence per line. Example:
ATGCGTAC
ATGNXGTA
GCTARGATN

2. Use the `sequence_summary()` function to analyze:

from sequence_cleaner import sequence_summary

sequence_summary("example_sequences.txt")


It will print:

- Total number of sequences

- Number of valid (clean) sequences

- Average GC content

- List of invalid sequences and characters
