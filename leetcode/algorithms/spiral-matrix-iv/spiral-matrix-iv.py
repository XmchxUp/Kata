from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1 for _ in range(n)] for _ in range(m)]
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        dir_idx = 0
        x, y = 0, 0
        while head:
            res[y][x] = head.val
            new_x, new_y = x + dirs[dir_idx][0], y + dirs[dir_idx][1]
            if (
                new_x < 0
                or new_y < 0
                or new_x >= n
                or new_y >= m
                or res[new_y][new_x] != -1
            ):
                dir_idx = (dir_idx + 1) % 4
                new_x, new_y = x + dirs[dir_idx][0], y + dirs[dir_idx][1]
            head = head.next
            x, y = new_x, new_y
        return res
