from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        assert len(intervals) >= 1
        intervals.sort(key=lambda e: e[0])

        lo, hi = intervals[0][0], intervals[0][1]
        res = []
        for i in range(1, len(intervals)):
            if intervals[i][0] <= hi:
                hi = max(hi, intervals[i][1])
            else:
                res.append([lo, hi])
                lo, hi = intervals[i][0], intervals[i][1]
        res.append([lo, hi])
        return res


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
