#include <vector>
using namespace std;

class Solution {
public:
  int majorityElement(vector<int> &nums) {
    int x = nums[0];
    int cnt = 0;
    for (int num : nums) {
      if (cnt == 0) {
        x = num;
        cnt = 1;
      } else if (num == x) {
        cnt++;
      } else {
        cnt--;
      }
    }
    return x;
  }
};