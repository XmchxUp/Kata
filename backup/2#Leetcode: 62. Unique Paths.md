# Leetcode: 62. Unique Paths

dp[i][j] = 到达i,j位置的唯一路径方案
dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

```py
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

```

---

* Link: https://github.com/XmchxUp/Kata/issues/2
* Labels: `bug`, `dp`
* Creation Date: 2024-01-01T01:08:15Z
