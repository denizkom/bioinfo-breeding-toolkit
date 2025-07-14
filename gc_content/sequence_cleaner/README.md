# Sequence Cleaner
This module validates and analyzes raw DNA sequences for use in genomic workflows.

##  Features
- Detects invalid characters in sequences
- Filters out non-ATGC sequences
- Calculates GC content of valid sequences
- Prints summary statistics

##How to Use

1. Prepare a plain text file with one sequence per line. Example:
ATGCGTAC
ATGNXGTA
GCTARGATN
2. Use the `sequence_summary()` function to analyze:
from sequence_cleaner import sequence_summary
sequence_summary("example_sequences.txt")
!!!!   ### FASTA Summary function added
from sequence_cleaner import fasta_summary
fasta_summary("example_fasta.fa")

It will print:
•	Total number of sequences
•	Number of valid sequences
•	Average GC content
•	Invalid sequences and problematic characters


Output Example: 
Total sequences: 6
Clean sequences: 2
Average GC content: 50.00%
Invalid sequences:
- ATGNXGTA → Invalid characters: {'N', 'X'}
- GCTARGATN → Invalid characters: {'R', 'N'}
