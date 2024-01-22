from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        actual_sum = sum(nums)
        unique_sum = sum(set(nums))
        expected_sum = (n + 1) * n // 2

        return [actual_sum - unique_sum, expected_sum - unique_sum]
