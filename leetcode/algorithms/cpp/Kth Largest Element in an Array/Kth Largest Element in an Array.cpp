#include <vector>
using namespace std;
class Solution {
public:
  int findKthLargest(vector<int> &nums, int k) {
    return quickSelect(nums, 0, nums.size() - 1, k);
  }
  int quickSelect(vector<int> &nums, int lo, int hi, int k) {
    if (lo >= hi) {
      return nums[lo];
    }
    int i = lo - 1, j = hi + 1, pivot = nums[lo];
    while (i < j) {
      do {
        i++;
      } while (nums[i] < pivot);
      do {
        j--;
      } while (nums[j] > pivot);
      if (i < j) {
        swap(nums[i], nums[j]);
      }
    }
    int cnt = hi - j;
    if (k <= cnt) {
      return quickSelect(nums, j + 1, hi, k);
    } else {
      return quickSelect(nums, lo, j, k - cnt);
    }
  }
};