from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        """
        1. 先统计元素出现的次数，最小的行数为最多的元素出现次数
        2. 遍历所有元素每次取一个
        """
        info = dict()
        for num in nums:
            info[num] = info.get(num, 0) + 1

        rows = max(info.values())
        res = [[] for _ in range(rows)]

        for i in range(rows):
            for k, v in info.items():
                if v > 0:
                    res[i].append(k)
                    info[k] -= 1
        return res


print(Solution().findMatrix([1, 3, 4, 1, 2, 3, 1]))
