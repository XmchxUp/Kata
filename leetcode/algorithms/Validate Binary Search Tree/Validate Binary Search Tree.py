# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    pre_val = None

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not self.isValidBST(root.left):
            return False
        if self.pre_val != None and root.val <= self.pre_val:
            return False
        self.pre_val = root.val
        return self.isValidBST(root.right)
