# Sequence Tools

A collection of Python functions for basic sequence quality control (QC) and content analysis.

## Features

- Read and clean raw nucleotide sequences from TXT or FASTA files
- Identify invalid characters in sequences
- Calculate GC and AT content
- Print summary statistics of clean and invalid sequences

## File: `sequence_qc.py`

### 🔹 Functions

- `read_sequences(path)`  
- `read_fasta(path)`  
- `is_valid(seq)`  
- `find_invalid_bases(seq)`  
- `calculate_gc(seq)`  
- `calculate_at(seq)`  
- `sequence_summary(path)`  
- `fasta_summary_with_at(path)`

## 💻 Example Usage
from sequence_qc import sequence_summary
sequence_summary("example_sequences.txt")

from sequence_qc import fasta_summary_with_at
fasta_summary_with_at("example_fasta.fa")

>seq1
ATGCGCTA
>seq2
GATTACAG
>seq3
ATGNXGTA

Total sequences: 3
Clean sequences: 2
Average GC content: 50.00%
Average AT content: 50.00%
Invalid sequences:
- seq3 -- Invalid characters: {'N', 'X'}

🔧 Requirements
No external libraries required.
Works on Python 3.6+

