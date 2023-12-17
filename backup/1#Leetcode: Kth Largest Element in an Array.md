# Leetcode: Kth Largest Element in an Array

- [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

- Quick Select思想
	- 随便选个pivot，区分小、等、大、于pivot的集合。
	- 通过集合里的元数里的个数判断

```python
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
```

---

* Link: https://github.com/XmchxUp/Kata/issues/1
* Labels: `Quick Select`
* Creation Date: 2023-12-17T12:36:18Z
