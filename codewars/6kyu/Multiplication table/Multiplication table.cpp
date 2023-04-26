#include <vector>

using namespace std;
vector<vector<int>> multiplication_table(int n) {
  size_t len = static_cast<size_t>(n);
  vector<vector<int>> res{len, vector<int>{len, 0}};
  int idx = 1;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      res[i][j] = idx;
      idx++;
    }
  }
  return res;
}