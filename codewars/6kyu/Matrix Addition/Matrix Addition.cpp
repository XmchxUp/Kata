#include <vector>

std::vector<std::vector<int>> matrixAddition(std::vector<std::vector<int>> a,
                                             std::vector<std::vector<int>> b) {
  // your code here
  auto n = a.size(), m = a[0].size();
  std::vector<std::vector<int>> res{n, std::vector<int>(m, 0)};
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      res[i][j] = a[i][j] + b[i][j];
    }
  }
  return res;
}