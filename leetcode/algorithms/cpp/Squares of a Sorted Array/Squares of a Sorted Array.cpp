#include <vector>

using namespace std;

class Solution {
public:
  vector<int> sortedSquares(vector<int> &nums) {
    int n = nums.size();
    int i = 0, j = n - 1;
    vector<int> ans(n, 0);
    for (int idx = j; idx >= 0; idx--) {
      if (nums[i] * nums[i] < nums[j] * nums[j]) {
        ans[idx] = nums[j] * nums[j];
        j--;
      } else {
        ans[idx] = nums[i] * nums[i];
        i++;
      }
    }
    return ans;
  }
};