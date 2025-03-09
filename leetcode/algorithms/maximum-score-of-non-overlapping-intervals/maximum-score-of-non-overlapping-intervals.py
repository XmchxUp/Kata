from bisect import bisect_left
from typing import List, Tuple


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        v = [(r, l, weight, i) for i, (l, r, weight) in enumerate(intervals)]
        v.sort(key=lambda x: x[0])

        f: List[List[Tuple]] = [
            [(0, []) for _ in range(5)] for _ in range(len(intervals) + 1)
        ]

        for i, (r, l, weight, idx) in enumerate(v):
            k = bisect_left(v, (l,), hi=i)
            for j in range(1, 5):
                s2, id2 = f[k][j - 1]
                f[i + 1][j] = min(f[i][j], (s2 - weight, sorted(id2 + [idx])))

        return f[-1][4][1]
