from collections import Counter

def find_it(seq):
    counter = Counter(seq)
    for k, v in counter.items():
        if v % 2 == 1:
            return k
    return None
