class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        m = len(s) // 2
        i, j = 0, m
        cnt_i, cnt_j = 0, 0
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        while i < m:
            if s[i] in vowels:
                cnt_i += 1
            if s[j] in vowels:
                cnt_j += 1
            i += 1
            j += 1
        return cnt_i == cnt_j
