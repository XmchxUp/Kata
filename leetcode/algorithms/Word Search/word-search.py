from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def helper(x: int, y: int, idx: int):
            if idx == len(word):
                return True
            if (
                x >= m
                or y >= n
                or x < 0
                or y < 0
                or visited[x][y]
                or board[x][y] != word[idx]
            ):
                return False

            visited[x][y] = True
            for dir in dirs:
                nx, ny = x + dir[0], y + dir[1]
                if helper(nx, ny, idx + 1):
                    return True
            visited[x][y] = False
            return False

        for i in range(m):
            for j in range(n):
                if helper(i, j, 0):
                    return True
        return False
