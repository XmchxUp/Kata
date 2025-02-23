from collections import defaultdict
from bisect import bisect_left
import math
from typing import List, Tuple


class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        if k == 0:
            return True

        pos = defaultdict(list)
        for i, c in enumerate(s):
            pos[c].append(i)

        graph = defaultdict(list)
        for i, p in pos.items():
            l, r = p[0], p[-1]
            for j, q in pos.items():
                if j == i:
                    continue
                # [l, r] contains j
                qi = bisect_left(q, l)
                if qi < len(q) and q[qi] <= r:
                    graph[i].append(j)

        def dfs(x: str) -> None:
            nonlocal l, r, vis
            vis.add(x)
            p = pos[x]
            l = min(l, p[0])
            r = max(r, p[-1])
            for y in graph[x]:
                if y not in vis:
                    dfs(y)

        intervals = []
        for i, p in pos.items():
            # 如果包含i，求出最终的区间
            vis = set()
            l, r = math.inf, 0
            dfs(i)
            # 不能选整个区间 [0, n-1]
            if l > 0 or r < len(s) - 1:
                intervals.append((l, r))

        return self.maxNonoverlapIntervals(intervals) >= k

    def maxNonoverlapIntervals(self, intervals: List[Tuple[int, int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        pre_r = -1
        for l, r in intervals:
            if l > pre_r:
                ans += 1
                pre_r = r
        return ans
