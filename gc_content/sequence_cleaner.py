# sequence_cleaner.py by DenizKOM
#Don't forget to note your path and be sure you are working on same environment with seq and py files. 
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

