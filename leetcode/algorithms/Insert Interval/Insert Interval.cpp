#include <vector>
using namespace std;

class Solution {
public:
  vector<vector<int>> insert(vector<vector<int>> &intervals,
                             vector<int> &newInterval) {
    vector<vector<int>> res;
    int n = intervals.size();
    int k = 0;
    while (k < n && intervals[k][1] < newInterval[0]) {
      res.push_back(intervals[k]);
      k++;
    }

    if (k < n) {
      newInterval[0] = min(intervals[k][0], newInterval[0]);
      while (k < n && intervals[k][0] <= newInterval[1]) {
        newInterval[1] = max(newInterval[1], intervals[k][1]);
        k++;
      }
    }
    res.push_back(newInterval);
    while (k < n) {
      res.push_back(intervals[k]);
      k++;
    }
    return res;
  }
};