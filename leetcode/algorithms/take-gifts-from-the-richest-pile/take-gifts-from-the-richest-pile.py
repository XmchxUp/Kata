from math import isqrt
from typing import List
from heapq import heappush, heappop, heapreplace, heapify


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        q = [-g for g in gifts]
        heapify(q)
        for _ in range(k):
            g = heappop(q)
            if -g == 1:
                heappush(q, g)
                break
            heappush(q, -isqrt(-g))

        return -sum(q)
