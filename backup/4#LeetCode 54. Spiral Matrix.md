# LeetCode 54. Spiral Matrix

模拟遍历右下左上，当遍历完所有元素结束。


```python
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
```

---

* Link: https://github.com/XmchxUp/Kata/issues/4
* Labels: `simulation`
* Creation Date: 2024-01-01T05:53:43Z
