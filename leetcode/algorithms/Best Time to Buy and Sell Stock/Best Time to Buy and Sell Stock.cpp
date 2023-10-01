#include <vector>

using namespace std;

class Solution {
public:
  int maxProfit(vector<int> &prices) {
    if (prices.size() == 0) {
      return 0;
    }
    int res = 0;
    int cur_min = prices[0];
    for (int &p : prices) {
      if (p > cur_min) {
        res = max(res, p - cur_min);
      } else {
        cur_min = p;
      }
    }
    return res;
  }
};