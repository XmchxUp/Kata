from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo, cur, hi = 0, 0, len(nums) - 1
        # [lo, hi] 全部都是1
        while cur <= hi:
            if nums[cur] == 0:
                nums[lo], nums[cur] = nums[cur], nums[lo]
                cur += 1
                lo += 1
            elif nums[cur] == 1:
                cur += 1
            else:
                nums[hi], nums[cur] = nums[cur], nums[hi]
                hi -= 1
