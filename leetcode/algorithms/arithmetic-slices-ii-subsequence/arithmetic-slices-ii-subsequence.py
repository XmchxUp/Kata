from collections import defaultdict
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        # dp[i][diff] -> 以nums[i]结束，diff的子序列个数
        dp = [defaultdict(int) for _ in range(n)]
        for i in range(n):
            for j in range(i):
                diff = nums[i]-nums[j]
                dp[i][diff] += 1 + dp[j][diff]
                res += 1 + dp[j][diff]

                # 这里可以优化，可以直接返回res 因为
                # res += dp[j][diff]
                # 当前有 两个元素 ,当dp[j][diff]有值时说明(没值默认为0)，j前面还有个元素k所以是符号要求的，直接相加，最后返回。
                # i 
                # j
                # k



        # 去掉长度小于3的子序列个数
        return res - ((n * (n - 1)) // 2)
