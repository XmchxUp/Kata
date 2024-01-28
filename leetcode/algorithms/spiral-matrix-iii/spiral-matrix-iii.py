from typing import List


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = [[rStart, cStart]]

        steps = 1
        dir_idx = 0

        r, c = rStart, cStart
        while len(res) < rows * cols:
            # 每走两个方向，就增加步数
            for _ in range(2):
                for i in range(steps):
                    r += dirs[dir_idx][0]
                    c += dirs[dir_idx][1]
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                dir_idx = (dir_idx + 1) % 4

            steps += 1
        return res
