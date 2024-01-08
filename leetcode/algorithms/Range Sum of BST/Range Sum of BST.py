from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        

    def rangeSumBSTV2(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        res = 0


        q = [root]
        while len(q):
            n = len(q)
            for _ in range(n):
                node = q.pop(0)
                if node.val >= low and node.val <= high:
                    res += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res
