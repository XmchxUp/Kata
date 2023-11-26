from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i, j = 0, n - 1
        while i < j:
            m = (i + j) >> 1
            if nums[m] > nums[n - 1]:
                i = m + 1
            else:
                j = m
        # p...n-1
        # 0...p
        p = i
        i, j = 0, n - 1
        if target >= nums[p] and target <= nums[n - 1]:
            i = p
        else:
            j = p
        while i <= j:
            m = ((j - i) >> 1) + i
            if nums[m] == target:
                return m
            elif nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        return -1


print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
