from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m, n = len(matrix), len(matrix[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        x, y = 0, 0
        dir_idx = 0

        def is_valid_coordinate(x, y):
            return not (x < 0 or x >= n or y < 0 or y >= m or visited[y][x])

        while len(res) < m * n:
            res.append(matrix[y][x])
            visited[y][x] = True
            delta_x, delta_y = dirs[dir_idx]
            if not is_valid_coordinate(x + delta_x, y + delta_y):
                dir_idx = (dir_idx + 1) % 4
                delta_x, delta_y = dirs[dir_idx]
            x, y = x + delta_x, y + delta_y

        return res


print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(Solution().spiralOrder([[1]]))
