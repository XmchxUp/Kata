#include <vector>
using namespace std;

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
  TreeNode *sortedArrayToBST(vector<int> &nums) {
    return buildBST(nums, 0, nums.size() - 1);
  }
  TreeNode *buildBST(vector<int> &nums, int i, int j) {
    if (i > j) {
      return nullptr;
    }
    if (i == j) {
      return new TreeNode(nums[i]);
    }
    size_t mid = (j - i) / 2 + i;
    TreeNode *node = new TreeNode(nums[mid]);
    node->left = buildBST(nums, i, mid - 1);
    node->right = buildBST(nums, mid + 1, j);
    return node;
  }
};