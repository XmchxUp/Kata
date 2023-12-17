from typing import List
import random


class Solution:
    def findKthLargestV2(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        left = [x for x in nums if x < pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]

        if k <= len(right):
            return self.findKthLargestV2(right, k)
        elif k > len(right) + len(mid):
            return self.findKthLargestV2(left, k - (len(right) + len(mid)))
        return mid[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(lo: int, hi: int, k: int):
            if lo >= hi:
                return nums[lo]
            x = nums[lo]
            i, j = lo - 1, hi + 1
            while i < j:
                i += 1
                while i <= j:
                    if nums[i] >= x:
                        break
                    i += 1
                j -= 1
                while j >= i:
                    if nums[j] <= x:
                        break
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            largeCnt = hi - j
            if k <= largeCnt:
                return quickSelect(j + 1, hi, k)
            else:
                return quickSelect(lo, j, k - largeCnt)

        return quickSelect(0, len(nums) - 1, k)


print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
