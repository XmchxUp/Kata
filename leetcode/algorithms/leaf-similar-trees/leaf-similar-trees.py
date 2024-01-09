from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def helper(node: Optional[TreeNode]):
            if not node: return []
            if not node.left and not node.right: return [node.val]
            return helper(node.left) + helper(node.right)
        return helper(root1) == helper(root2)
