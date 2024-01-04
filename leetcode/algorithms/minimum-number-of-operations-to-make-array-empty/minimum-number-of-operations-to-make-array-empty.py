from typing import List
from collections import Counter


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        除了1，任何正整数都可以由任意个3和2组成。
        先按三个数消除，如果还多的数，无法就两种情况
            1. 还剩1个数 
            2. 还剩2个数
        都等于再加一次两个数消除
        """
        cnts = Counter(nums)

        res = 0
        for cnt in cnts.values():
            if cnt == 1:
                return -1
            res += cnt // 3
            if cnt % 3:
                res += 1

        return res


print(Solution().minOperations([2, 3, 3, 2, 2, 4, 2, 3, 4]))
