from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        dp[i]: 表示0..i中包含元素nums[i]的最长子窜
        dp[i] = 对于每个dp[0..i]元素 加当前元素nums[i]
        """
        n = len(nums)
        dp = [1] * len(nums)
        res = 1
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            res = max(res, dp[i])
    
        return res
