#include <vector>
using namespace std;

// https://leetcode.cn/problems/maximum-absolute-sum-of-any-subarray/solutions/867508/javaliang-chong-jie-fa-dong-tai-gui-hua-k8iry/

class Solution {
public:
  // ma当前最大的子数组和
  // mi当前最小的子数组和
  int maxAbsoluteSum(vector<int> &nums) {
    int ma = nums[0], mi = nums[0];

    int ans = std::abs(nums[0]);
    for (int i = 1; i < nums.size(); i++) {
      ma = std::max(nums[i], ma + nums[i]);
      mi = std::min(nums[i], mi + nums[i]);

      ans = std::max(ans, std::max(std::abs(ma), std::abs(mi)));
    }
    return ans;
  }

  // 前缀和
  int maxAbsoluteSumV2(vector<int> &nums) {
    int sum = 0;
    int ma = 0, mi = 0;
    for (int i = 1; i <= nums.size(); i++) {
      sum += nums[i - 1];
      if (ma < sum) {
        ma = sum;
      }
      if (mi > sum) {
        mi = sum;
      }
    }
    return ma - mi;
  }
};