#include <vector>

using namespace std;

class Solution {
private:
  const int MAX_ELEMENT_SIZE = 1e5 + 10;

public:
  int minSubArrayLen(int target, vector<int> &nums) {
    int n = nums.size();
    int i = 0, j = 0;
    int sum = 0, res = MAX_ELEMENT_SIZE;
    while (i < n) {
      sum += nums[i];
      i++;
      while (sum >= target) {
        res = std::min(res, i - j);
        sum -= nums[j];
        j++;
      }
    }
    if (sum >= target) {
      res = std::min(res, i - j);
    }
    return res == MAX_ELEMENT_SIZE ? 0 : res;
  }
};