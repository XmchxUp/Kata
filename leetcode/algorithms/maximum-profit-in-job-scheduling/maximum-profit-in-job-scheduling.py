from typing import List
import bisect


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        f = [0] * (len(jobs) + 1)

        for i, (_, st, p) in enumerate(jobs):
            j = bisect.bisect_left(jobs, (st + 1,), hi=i)
            f[i + 1] = max(f[i], f[j] + p)

        return f[-1]

    def jobScheduling2(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        """
        DFS搜索: 对当前i job是否选或不选两种情况遍历。
        """
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}

        def dfs(i: int):
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]

            # dont include i job
            res = dfs(i + 1)

            # include i job
            # j = i + 1
            # while j < len(intervals):
            #     if intervals[i][1] <= intervals[j][0]:
            #         break
            #     j += 1
            j = bisect.bisect_left(intervals, (intervals[i][1], -1, -1))
            cache[i] = res = max(res, intervals[i][2] + dfs(j))

            return res

        return dfs(0)
