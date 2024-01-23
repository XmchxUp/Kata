from collections import Counter
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        """
        BackTrack
        Time Complexity: O(2*N)
        Space Complexity: O(N)

        """
        charSet = set()

        def overlap(charSet, s):
            c = Counter(charSet) + Counter(s)
            return max(c.values()) > 1
            prev = set()
            for c in s:
                if c in charSet or c in prev:
                    return True
                prev.add(c)
            return False

        def backtrack(idx: int):
            if idx == len(arr):
                return len(charSet)

            res = 0
            if not overlap(charSet, arr[idx]):  # 选择arr[idx]
                for c in arr[idx]:
                    charSet.add(c)
                res = backtrack(idx + 1)
                for c in arr[idx]:
                    charSet.remove(c)

            return max(res, backtrack(idx + 1))

        return backtrack(0)

    def maxLengthV1(self, arr: List[str]) -> int:
        """
        Bitmap
        N = len(arr)
        M = maximum length of a string in arr
        Time Complexity: O(N * M)
        Space Complexity: O(2^M)

        [x, y, z]
        000
        001
        ...
        111
        """
        dp = [0]
        res = 0

        for ele in arr:
            x = 0
            dup = 0
            for c in ele:
                tmp = 1 << (ord(c) - ord("a"))
                dup |= x & tmp
                x |= tmp
            if dup > 0:
                continue
            n = len(dp)
            for i in range(n - 1, -1, -1):
                if (dp[i] & x) > 0:
                    continue
                dp.append(dp[i] | x)
                res = max(res, bin(dp[i] | x).count("1"))
        return res
