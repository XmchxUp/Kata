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
  bool isBalanced(TreeNode *root) {
    if (root == nullptr) {
      return true;
    }
    if (std::abs(getHeight(root->left) - getHeight(root->right)) > 1) {
      return false;
    }
    return isBalanced(root->left) && isBalanced(root->right);
  }
  int getHeight(TreeNode *p) {
    if (p == nullptr) {
      return 0;
    }
    return 1 + std::max(getHeight(p->left), getHeight(p->right));
  }
};