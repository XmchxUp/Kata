from typing import List
from math import inf


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        res = 0
        pre_r = -inf
        for l, r in intervals:
            if l >= pre_r:
                res += 1
                pre_r = r
        return len(intervals) - res
