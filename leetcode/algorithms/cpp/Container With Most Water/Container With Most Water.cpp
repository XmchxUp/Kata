#include <vector>
using namespace std;

class Solution {
public:
  int maxArea(vector<int> &height) {
    int n = height.size();
    int i = 0, j = n - 1;
    int max_area = 0;
    while (i < j) {
      max_area = std::max(max_area, (j - i) * std::min(height[i], height[j]));
      if (height[i] < height[j]) {
        i++;
      } else {
        j--;
      }
    }
    return max_area;
  }
};