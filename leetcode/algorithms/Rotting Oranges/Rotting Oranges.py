from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]

        m = len(grid)
        n = len(grid[0])

        q = []
        fresh_cnt = 0
        zero_cnt = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh_cnt += 1
                else:
                    zero_cnt += 1
        if zero_cnt == m * n:
            return 0

        res = 0
        while len(q) > 0:
            new_q = []
            for x, y in q:
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] != 1:
                        continue
                    fresh_cnt -= 1
                    grid[nx][ny] = 2
                    new_q.append((nx, ny))
            res += 1
            q = new_q

        if fresh_cnt == 0:
            return res - 1
        else:
            return -1


print(Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
