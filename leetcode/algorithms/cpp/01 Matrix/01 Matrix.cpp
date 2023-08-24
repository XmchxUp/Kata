#include <queue>
#include <vector>

using namespace std;

class Solution {
public:
  vector<vector<int>> updateMatrix(vector<vector<int>> &mat) {
    int m = mat.size(), n = mat[0].size();
    int dx[4] = {0, 0, 1, -1}, dy[4] = {1, -1, 0, 0};
    vector<vector<int>> dist(m, vector<int>(n, -1));
    queue<pair<int, int>> q;
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (mat[i][j] == 0) {
          dist[i][j] = 0;
          q.push({i, j});
        }
      }
    }
    while (!q.empty()) {
      auto curr = q.front();
      q.pop();
      for (int k = 0; k < 4; k++) {
        int neightbor_i = dx[k] + curr.first, neightbor_j = dy[k] + curr.second;
        if (neightbor_i < 0 || neightbor_j < 0 || neightbor_i >= m ||
            neightbor_j >= n || dist[neightbor_i][neightbor_j] != -1) {
          continue;
        }
        dist[neightbor_i][neightbor_j] = dist[curr.first][curr.second] + 1;
        q.push({neightbor_i, neightbor_j});
      }
    }
    return dist;
  }
};