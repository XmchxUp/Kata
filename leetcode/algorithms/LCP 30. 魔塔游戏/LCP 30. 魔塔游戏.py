from typing import List
from heapq import heappush, heappop


class Solution:
    def magicTower(self, nums: List[int]) -> int:
        if sum(nums) < 0:
            return -1

        hp = 1
        res = 0
        h = []

        for x in nums:
            if x < 0:
                heappush(h, x)

            hp += x
            if hp < 1:
                hp -= heappop(h)
                res += 1

        return res
