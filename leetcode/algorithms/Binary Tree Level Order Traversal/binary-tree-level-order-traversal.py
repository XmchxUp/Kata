# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        q = [root]
        while len(q) > 0:
            n = len(q)
            tmp_q = []
            tmp_val = []
            for i in range(n):
                node = q[i]
                tmp_val.append(node.val)
                if node.left:
                    tmp_q.append(node.left)
                if node.right:
                    tmp_q.append(node.right)
            res.append(tmp_val)
            q = tmp_q
        return res
