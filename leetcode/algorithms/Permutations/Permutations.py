from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        m = {}

        def helper(cur_nums: List[int]):
            if len(cur_nums) == len(nums):
                res.append(list(cur_nums))
                return

            for num in nums:
                if m.get(num, False):
                    continue
                m[num] = True
                helper(cur_nums + [num])
                m[num] = False

        helper([])
        return res


print(Solution().permute([1, 2, 3]))
