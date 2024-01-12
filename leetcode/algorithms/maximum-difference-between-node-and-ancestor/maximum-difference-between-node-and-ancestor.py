from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def helper(node: Optional[TreeNode], curr_max: int, curr_min: int):
            if not node:
                return curr_max - curr_min

            curr_min = min(curr_min, node.val)
            curr_max = max(curr_max, node.val)

            return max(
                helper(node.left, curr_max, curr_min),
                helper(node.right, curr_max, curr_min),
            )

        return helper(root, root.val, root.val)
