# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    last_ele = None

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        if not root.left and not root.right:
            return root

        fright = self.flatten(root.right)
        if not root.left:
            return root

        fleft = self.flatten(root.left)

        last_right = fleft
        while last_right.right:
            last_right = last_right.right

        last_right.right = fright
        root.right = fleft
        root.left = None

        return root
