class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")

        vowel_chs = []
        vowel_pos = []
        for i, ch in enumerate(s):
            if ch in vowels:
                vowel_chs.append(ch)
                vowel_pos.append(i)

        vowel_chs.sort()

        result = list(s)

        for pos, vowel in zip(vowel_pos, vowel_chs):
            result[pos] = vowel

        return "".join(result)
