from heapq import heappush, heappop
from math import sqrt


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = dict()
        q = []
        res = []
        for p in points:
            d = sqrt(p[0] ** 2 + p[1] ** 2)
            if d not in m:
                m[d] = []
            m[d].append(p)
            heappush(q, -d)
            if len(q) > k:
                heappop(q)

        for d in set(q):
            for p in m[-d]:
                res.append(p)
        return res
