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
  int maxDepth(TreeNode *root) { return getDepth(root); }

  int getDepth(TreeNode *node) {
    if (node == nullptr) {
      return 0;
    }

    return std::max(getDepth(node->left), getDepth(node->right)) + 1;
  }
};