from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        通过中序遍历确定当前节点左子树或右子树节点的个数
        """
        if len(inorder) == 0:
            return None

        val = preorder[0]
        idx = inorder.index(val)

        node = TreeNode(
            val,
            self.buildTree(preorder[1 : idx + 1], inorder[:idx]),
            self.buildTree(preorder[idx + 1 :], inorder[idx + 1 :]),
        )

        return node


print(Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
