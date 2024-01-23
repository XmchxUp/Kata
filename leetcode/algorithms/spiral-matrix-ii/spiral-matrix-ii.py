from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]

        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        x, y = 0, 0
        dir_idx = 0

        def is_valid_coordinate(x, y):
            return not (x < 0 or x >= n or y < 0 or y >= n or res[y][x] != 0)

        for i in range(n * n):
            res[y][x] = i + 1
            delta_x, delta_y = dirs[dir_idx]
            if not is_valid_coordinate(x + delta_x, y + delta_y):
                dir_idx = (dir_idx + 1) % 4
                delta_x, delta_y = dirs[dir_idx]
            x, y = x + delta_x, y + delta_y

        return res
