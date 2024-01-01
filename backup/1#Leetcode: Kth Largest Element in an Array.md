# Leetcode: Kth Largest Element in an Array

- [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

- Quick Select思想
	- 随便选个pivot，区分小、等、大、于pivot的集合。
	- 通过集合里的元数里的个数判断

```python
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

```

---

* Link: https://github.com/XmchxUp/Kata/issues/1
* Labels: `Quick Select`
* Creation Date: 2023-12-17T12:36:18Z
