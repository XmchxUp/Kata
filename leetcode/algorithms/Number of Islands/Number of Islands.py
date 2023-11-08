from typing import List


class Solution:
    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    self.dfs(grid, i, j)

        return res

    def dfs(self, grid: List[List[str]], i: int, j: int) -> None:
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
            return
        grid[i][j] = "0"
        for dir in self.directions:
            self.dfs(grid, i + dir[0], j + dir[1])
