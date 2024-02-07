from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        q = [root]

        while q:
            next_level_sum = 0
            tmp_q = []

            for node in q:
                if node.left:
                    next_level_sum += node.left.val
                    tmp_q.append(node.left)

                if node.right:
                    next_level_sum += node.right.val
                    tmp_q.append(node.right)

            for node in q:
                child_sum = 0
                if node.left:
                    child_sum += node.left.val

                if node.right:
                    child_sum += node.right.val

                if node.left:
                    node.left.val = next_level_sum - child_sum
                if node.right:
                    node.right.val = next_level_sum - child_sum

            q = tmp_q
        return root
