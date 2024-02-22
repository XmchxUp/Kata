from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(i: int, j: int):
            if i > j:
                return None

            if i == j:
                return TreeNode(val=nums[i])

            mid = (j - i) // 2 + i
            mid_node = TreeNode(val=nums[mid])

            mid_node.left = helper(i, mid - 1)
            mid_node.right = helper(mid + 1, j)

            return mid_node

        return helper(0, len(nums) - 1)
