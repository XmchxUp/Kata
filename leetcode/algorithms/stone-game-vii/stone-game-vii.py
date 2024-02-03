from itertools import accumulate
from typing import List


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        prev_sums = list(accumulate(stones, initial=0))
        f = [[0] * n for _ in range(n)]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = max(
                    prev_sums[j + 1] - prev_sums[i + 1] - f[i + 1][j],
                    prev_sums[j] - prev_sums[i] - f[i][j - 1],
                )
        return f[0][-1]
