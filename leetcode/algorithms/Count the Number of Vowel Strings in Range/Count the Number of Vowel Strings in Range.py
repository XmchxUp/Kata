from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowel_set = set(["a", "e", "i", "o", "u"])
        cnt = 0
        for i in range(left, right + 1):
            if words[i][0] in vowel_set and words[i][-1] in vowel_set:
                cnt += 1
        return cnt
