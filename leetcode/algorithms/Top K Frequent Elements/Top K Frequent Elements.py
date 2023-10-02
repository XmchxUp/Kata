from heapq import heappush, heappop
from collections import Counter


# 桶排序
# Time Complexity O(n)
# Space Complexity O(n)
class Solution2(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        m = dict()
        for num in nums:
            if num not in m:
                m[num] = 0
            m[num] += 1
        tmpArr = [[] for _ in range((len(nums) + 1))]
        for num, freq in m.items():
            tmpArr[freq].append(num)
        res = []
        size = k
        for i in range(len(tmpArr) - 1, 0, -1):
            if k == 0:
                break
            if tmpArr[i]:
                res += tmpArr[i]
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
