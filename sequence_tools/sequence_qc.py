"""
Created on Mon Jul 14 09:46:53 2025

@author: denizkom
"""
"""
sequence_qc.py by DenizKOM
Clean and analyze raw nucleotide sequences from TXT and FASTA formats.
"""
# Sequence quality control utilities — content to be uploaded

import os

valid_bases = {"A", "T", "G", "C"}


def is_valid(seq):
    """
    Check whether a sequence contains only valid bases (A, T, G, C).
    """
    return set(seq) <= valid_bases


def find_invalid_bases(seq):
    """
    Identify invalid characters in a sequence.
    Returns a set of characters not in valid_bases.
    """
    return set(seq) - valid_bases


def calculate_gc(seq):
    """
    Calculate GC percentage of a nucleotide sequence.
    Returns a float between 0–100.
    """
    gc_count = seq.count("G") + seq.count("C")
    return (gc_count / len(seq)) * 100 if seq else 0


def calculate_at(seq):
    """
    Calculate AT percentage of a nucleotide sequence.
    Returns a float between 0–100.
    """
    at_count = seq.count("A") + seq.count("T")
    return (at_count / len(seq)) * 100 if seq else 0


def read_sequences(path):
    """
    Read plain text file line by line, ignoring empty lines.
    Yields one cleaned sequence per line.
    """
    with open(path, "r") as f:
        for line in f:
            seq = line.strip()
            if not seq:
                continue
            yield seq


def read_fasta(path):
    """
    Read FASTA-formatted file.
    Yields tuples of (sequence_id, sequence).
    """
    if not os.path.isfile(path):
        print("‼️ File cannot be located:", path)
        print("Current directory:", os.getcwd())
        print("Files in current directory:", os.listdir())
        return []

    with open(path, "r") as f:
        seq_id = None
        seq = ""
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if seq_id:
                    yield (seq_id, seq)
                seq_id = line[1:]
                seq = ""
            else:
                seq += line
        if seq_id:
            yield (seq_id, seq)


def sequence_summary(path):
    """
    Summarize sequences from a TXT file.
    Prints total, clean, average GC, and lists invalid sequences.
    """
    total = 0
    clean = 0
    gc_values = []
    dirty_list = []

    for seq in read_sequences(path):
        total += 1
        if is_valid(seq):
            clean += 1
            gc_values.append(calculate_gc(seq))
        else:
            dirty_list.append((seq, find_invalid_bases(seq)))

    print(f"Total sequences: {total}")
    print(f"Clean sequences: {clean}")
    if gc_values:
        avg_gc = sum(gc_values) / len(gc_values)
        print(f"Average GC content: {avg_gc:.2f}%")
    if dirty_list:
        print("Invalid sequences:")
        for seq, invalid in dirty_list:
            print(f"- {seq} → Invalid characters: {invalid}")


def fasta_summary_with_at(path):
    """
    Summarize sequences from a FASTA file.
    Prints total, clean, average GC & AT, and lists invalid sequences.
    """
    print("FASTA summary with AT and GC started.")
    total = 0
    clean = 0
    gc_values = []
    at_values = []
    invalids = []

    for seq_id, seq in read_fasta(path):
        total += 1
        if is_valid(seq):
            clean += 1
            gc_values.append(calculate_gc(seq))
            at_values.append(calculate_at(seq))
        else:
            invalid_chars = find_invalid_bases(seq)
            invalids.append((seq_id, invalid_chars))

    print(f"Total sequences: {total}")
    print(f"Clean sequences: {clean}")
    if gc_values:
        avg_gc = sum(gc_values) / len(gc_values)
        print(f"Average GC content: {avg_gc:.2f}%")
    if at_values:
        avg_at = sum(at_values) / len(at_values)
        print(f"Average AT content: {avg_at:.2f}%")
    if invalids:
        print("Invalid sequences:")
        for seq_id, invalid_chars in invalids:
            print(f"- {seq_id} -- Invalid characters: {invalid_chars}")

