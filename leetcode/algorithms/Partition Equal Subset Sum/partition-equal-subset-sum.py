from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        m = sum(nums)
        if m % 2 != 0:
            return False
        m //= 2
        f = [0] * (m + 1)
        f[0] = 1
        for x in nums:
            for j in range(m, x - 1, -1):
                f[j] = f[j] | f[j-x]
        return f[m] == 1
