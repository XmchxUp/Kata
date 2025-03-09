class Solution:
    def calculateScore(self, s: str) -> int:
        sts = [[] for _ in range(26)]
        res = 0

        for i, c in enumerate(s):
            idx = ord(c) - ord("a")
            target = 25 - idx
            if len(sts[target]) > 0:
                res += i - sts[target].pop()
            else:
                sts[idx].append(i)

        return res
