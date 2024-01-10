from typing import Optional
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root:
            return 0

        # build node connection info
        # {node: [parent, left-child, right-child]}
        info = defaultdict(list)

        q = [root]
        parent_info = {root: None}
        while len(q):
            n = len(q)
            for _ in range(n):
                node = q.pop(0)
                if parent_info[node]:
                    info[node.val].append(parent_info[node].val)
                if node.left:
                    q.append(node.left)
                    info[node.val].append(node.left.val)
                    parent_info[node.left] = node
                if node.right:
                    q.append(node.right)
                    info[node.val].append(node.right.val)
                    parent_info[node.right] = node

        q = [(info[start], 0)]
        visited = set([start])
        last_minute = 0
        while len(q):
            n = len(q)
            for _ in range(n):
                nodes, minute = q.pop(0)
                last_minute = minute
                for node in nodes:
                    if node in visited:
                        continue
                    q.append((info[node], minute + 1))
                    visited.add(node)
        return last_minute
