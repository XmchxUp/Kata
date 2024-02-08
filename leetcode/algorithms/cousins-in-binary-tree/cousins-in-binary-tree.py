from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def helper(node: Optional[TreeNode], depth: int, val: int):
            if not node:
                return (None, -1)
            if (node.left and node.left.val == val) or (
                node.right and node.right.val == val
            ):
                return (node, depth + 1)

            res = helper(node.left, depth + 1, val)
            if res[0]:
                return res
            return helper(node.right, depth + 1, val)

        res_x = helper(root, 0, x)
        res_y = helper(root, 0, y)
        return res_x[1] == res_y[1] and res_x[0] != res_y[0]
