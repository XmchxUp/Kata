from typing import List
from heapq import heappush, heappop
from collections import Counter, defaultdict


# 桶排序
# Time Complexity O(n)
# Space Complexity O(n)
class Solution2(object):
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        freq_arr = [[] for _ in range(len(nums) + 1)]
        for num, freq in d.items():
            freq_arr[freq].append(num)
        res = []
        size = k
        for i in range(len(freq_arr) - 1, 0, -1):
            if k == 0:
                break
            if len(freq_arr[i]) > 0:
                res += freq_arr[i]
                k -= 1
        return res[:size]


# 最小堆
# Time Complexity O(NlogK)
# Space Complexity O(N)
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
