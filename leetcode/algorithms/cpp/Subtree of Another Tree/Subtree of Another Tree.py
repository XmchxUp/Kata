# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isSameTree(self, n1, n2):
        if not n1 and not n2:
            return True
        elif not n1 or not n2:
            return False
        return (
            n1.val == n2.val
            and self.isSameTree(n1.left, n2.left)
            and self.isSameTree(n1.right, n2.right)
        )

    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
