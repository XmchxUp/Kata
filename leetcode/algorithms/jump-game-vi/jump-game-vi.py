from collections import deque
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [0] * n
        f[0] = nums[0]
        q = deque([0])
        for i in range(1, n):
            if i - q[0] > k:
                q.popleft()
            f[i] = f[q[0]] + nums[i]
            while q and f[i] >= f[q[-1]]:
                q.pop()
            q.append(i)
        return f[-1]

    def maxResultV1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [0] * n
        f[0] = nums[0]

        for i in range(1, n):
            f[i] = max(f[max(i - k, 0) : i]) + nums[i]
        return f[-1]
