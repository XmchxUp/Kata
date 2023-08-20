#include <vector>
using namespace std;

class Solution {
public:
  int maxSubArray(vector<int> &nums) {
    int res = nums[0];
    int last = nums[0];
    for (int i = 1; i < nums.size(); i++) {
      last = std::max(nums[i], last + nums[i]);
      res = std::max(res, last);
    }
    return res;
  }
  int maxSubArrayV2(vector<int> &nums) {
    return maxSubArray(nums, 0, nums.size() - 1);
  }

  // 最大子数组和在这三个区间中的一个
  // [left, mid]
  // [mid+1, right]
  // [left, mid, right]
  int maxSubArray(vector<int> &nums, int lo, int hi) {
    if (lo == hi) {
      return nums[lo];
    }
    int mid = ((hi - lo) >> 1) + lo;
    int max_left_sub_array = maxSubArray(nums, lo, mid);
    int max_right_sub_array = maxSubArray(nums, mid + 1, hi);

    int max_all_sub_array = 0;
    int curr_max_sum = nums[mid];
    int curr_sum = nums[mid];
    for (int i = mid - 1; i >= lo; i--) {
      curr_sum += nums[i];
      curr_max_sum = std::max(curr_sum, curr_max_sum);
    }

    max_all_sub_array += curr_max_sum;
    curr_sum = curr_max_sum = nums[mid + 1];
    for (int i = mid + 2; i <= hi; i++) {
      curr_sum += nums[i];
      curr_max_sum = std::max(curr_sum, curr_max_sum);
    }
    max_all_sub_array += curr_max_sum;

    return std::max(max_all_sub_array,
                    std::max(max_left_sub_array, max_right_sub_array));
  }
};