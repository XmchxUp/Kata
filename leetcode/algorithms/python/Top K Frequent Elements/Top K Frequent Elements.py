from heapq import heappush, heappop
from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)
        max_q = []
        for num in counter:
            heappush(max_q, (-counter[num], num))
        res = []
        for _ in range(k):
            res.append(heappop(max_q)[1])
        return res
