#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
  bool containsDuplicate(vector<int> &nums) {
    unordered_map<int, int> cnts{};
    for (int num : nums) {
      cnts[num]++;
      if (cnts[num] >= 2) {
        return true;
      }
    }
    return false;
  }
};