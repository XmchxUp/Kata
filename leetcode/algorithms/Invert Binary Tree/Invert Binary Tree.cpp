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
  TreeNode *invertTree(TreeNode *root) {
    if (root == nullptr)
      return nullptr;
    auto p1 = invertTree(root->left);
    auto p2 = invertTree(root->right);
    root->left = p2;
    root->right = p1;
    return root;
  }
};