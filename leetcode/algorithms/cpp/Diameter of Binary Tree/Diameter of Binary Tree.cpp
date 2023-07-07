#include <iostream>
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

class Solution {
public:
  int diameterOfBinaryTree(TreeNode *root) {
    if (root == nullptr) {
      return 0;
    }
    int cur = getHeightOfTree(root->left) + getHeightOfTree(root->right);
    int leftVal = diameterOfBinaryTree(root->left);
    int rightVal = diameterOfBinaryTree(root->right);
    return std::max(std::max(cur, leftVal), rightVal);
  }
  int getHeightOfTree(TreeNode *node) {
    if (node == nullptr) {
      return 0;
    }
    return 1 +
           std::max(getHeightOfTree(node->left), getHeightOfTree(node->right));
  }
};