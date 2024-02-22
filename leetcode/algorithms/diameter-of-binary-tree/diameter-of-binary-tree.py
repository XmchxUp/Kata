from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return max(self.max_depth(node.left), self.max_depth(node.right)) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # TODO: 优化使用个全局变量，来记录最大的值，不需要在这里在递归遍历了
        return max(
            self.max_depth(root.left) + self.max_depth(root.right),
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right),
        )
