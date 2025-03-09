from math import lcm, gcd
from typing import List


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        all_lcm = lcm(*nums)
        res = 0
        for i in range(len(nums)):
            p, g, l = 1, 0, 1
            for j in range(i, len(nums)):
                x = nums[j]
                p *= x
                l = lcm(l, x)
                g = gcd(g, x)
                if p == l * g:
                    res = max(res, j - i + 1)
                if p > all_lcm * g:
                    break
        return res
