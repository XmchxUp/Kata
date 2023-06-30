#include <vector>

using namespace std;

class Solution {
public:
  // 88/215

  void sortColors(vector<int> &nums) {
    // nums[0..zero] 0
    // nums[zero+1,two-1] 1
    // nums[two, n-1] 2
    size_t n = nums.size();
    int zero = -1, two = n;
    for (int i = 0; i < two;) {
      if (nums[i] == 1) {
        i++;
      } else if (nums[i] == 2) {
        swap(nums[--two], nums[i]);
      } else { // 0
        assert(nums[i] == 0);
        swap(nums[++zero], nums[i++]);
      }
    }
  }
};