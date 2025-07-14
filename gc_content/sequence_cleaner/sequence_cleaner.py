"""
Created on Mon Jul 14 09:46:53 2025

@author: denizkom
"""
"""
# sequence_cleaner.py by DenizKOM
# Don't forget to note your path and be sure you are working on same environment with seq and py files. 
# some lines have their explanations for me to remember :) 
"""
valid = {"A", "T", "G", "C"}
def read_sequences(path):
    with open(path, "r") as f:
        for line in f:
            seq = line.strip()
            if not seq:
                continue
            yield seq

def is_valid(seq):
    return set(seq) <= valid

def find_invalid_bases(seq):
    return set(seq) - valid

def calculate_gc(seq):
    gc_count = seq.count("G") + seq.count("C")
    return (gc_count / len(seq)) * 100 if seq else 0

def sequence_summary(path):
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
    print("Invalid sequences:")
    for seq, invalid in dirty_list:
        print(f"- {seq} → Invalid characters: {invalid}")

import os

def read_fasta(path):
    if not os.path.isfile(path):
        print("‼️ Dosya bulunamadı:", path)
        print("🔎 Current directory:", os.getcwd())
        print("📁 Files in current directory:", os.listdir())
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
"""
# Reads the FASTA file and analysis valid and invalid sequences. 
# Calculates average GC% in valid sequences.
# Lists invalid characters in invalid sequences. 
"""
def fasta_summary(path):
    print("fasta_summary started")
    valid_bases = {"A", "T", "G", "C"}
    total = 0         # total number of sequences
    clean = 0         # number of valid sequences
    gc_values = []    # GC percentages of valid sequences
    invalids = []     # list of invalid sequences and their problems
    for seq_id, seq in read_fasta(path):    ## Read each sequence from FASTA file (returns ID and sequence separately)
        total +=1
        if is_valid(seq):
            clean +=1
            gc = calculate_gc(seq)
            gc_values.append(gc)
        else:
            invalid_chars = set(seq) - valid_bases
            invalids.append((seq_id, invalid_chars))
    print(f"Total number of sequences: {total}")   #General stats.
    print(f"Clean sequences: {clean}")
    if gc_values:  #works with clean sequences
        avg_gc = sum(gc_values) / len(gc_values)
        print(f"Average GC Content is: {avg_gc:.2f}")
    if invalids: #works with invalid sequences
        print("Invalid Sequences: ")
        for seq_id, invalid_chars in invalids:
            print(f"- {seq_id} -- Invalid Chars.: {invalid_chars}")

 # End of sequence_cleaner.py   
    

