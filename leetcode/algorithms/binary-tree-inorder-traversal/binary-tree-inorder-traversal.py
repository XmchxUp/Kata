from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def helper(node: Optional[TreeNode]):
            if not node:
                return

            helper(node.left)
            res.append(node.val)
            helper(node.right)

        helper(root)
        return res
