from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()

        def helper(idx: int, curr_sum: int, curr_vals: List[int]):
            nonlocal res
            if curr_sum > target:
                return
            elif curr_sum == target:
                res.append(list(curr_vals))
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                curr_vals.append(candidates[i])
                helper(i, curr_sum + candidates[i], curr_vals)
                curr_vals.pop()

        helper(0, 0, [])
        return res


print(Solution().combinationSum([2, 3, 6, 7], 7))
