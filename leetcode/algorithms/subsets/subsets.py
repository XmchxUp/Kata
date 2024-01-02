from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(curr_idx: int, curr_nums: List[int]):
            res.append(list(curr_nums))
            for i in range(curr_idx, len(nums)):
                curr_nums.append(nums[i])
                helper(i + 1, curr_nums)
                curr_nums.pop()

        helper(0, [])
        return res


print(Solution().subsets([0]))
print(Solution().subsets([1, 2, 3]))
