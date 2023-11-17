from heapq import heappush, heappop


class Node:
    default_val = "."

    def __init__(self, freq, val=default_val, left=None, right=None):
        self.freq_ = freq
        self.val_ = val
        self.left_ = left
        self.right_ = right

    def __lt__(self, other):
        return self.val_ < other.val_


def build_tree(freqs):
    min_q = []
    for val, freq in freqs:
        heappush(min_q, (freq, Node(freq, val)))

    while len(min_q) > 1:
        freq1, node1 = heappop(min_q)
        freq2, node2 = heappop(min_q)
        merged_freq = freq1 + freq2
        merged_node = Node(merged_freq, left=node1, right=node2)
        heappush(min_q, (merged_freq, merged_node))
    return min_q[0][1]


def generate_code(tree):
    codes = {}

    def traverse(node, code):
        if node.val_ != Node.default_val:
            codes[node.val_] = code

        if node.left_:
            traverse(node.left_, code + "0")
        if node.right_:
            traverse(node.right_, code + "1")

    traverse(tree, "")
    return codes


# takes: str; returns: [ (str, int) ] (Strings in return value are single characters)
def frequencies(s: str):
    return list(map(lambda c: (c, s.count(c)), set(s)))


# takes: [ (str, int) ], str; returns: String (with "0" and "1")
def encode(freqs, s):
    if len(freqs) <= 1:
        return None
    tree = build_tree(freqs)
    codes = generate_code(tree)
    res = ""
    for c in s:
        res += codes[c]
    return res


# takes [ [str, int] ], str (with "0" and "1"); returns: str
def decode(freqs, bits):
    if len(freqs) <= 1:
        return None
    root = build_tree(freqs)
    res = ""
    curr = root
    for b in bits:
        if b == "0":
            curr = curr.left_
        else:
            curr = curr.right_
        if curr.val_ != Node.default_val:
            res += curr.val_
            curr = root
    return res


if __name__ == "__main__":
    s = "aaaabcc"
    fqs = frequencies(s)
    bits = encode(fqs, s)
    print(decode(fqs, bits))
