class Node:
    def __init__(self) -> None:
        self.chs = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        prev = self.root
        for ch in word:
            if ch not in prev.chs:
                prev.chs[ch] = Node()
            prev = prev.chs[ch]
        prev.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.chs:
                return False
            node = node.chs[ch]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.chs:
                return False
            node = node.chs[ch]
        return len(node.chs) > 0 or node.is_word
