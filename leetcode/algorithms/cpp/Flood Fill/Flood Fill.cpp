#include <vector>
using namespace std;
class Solution {
private:
  int dirs[4][2] = {
      {-1, 0},
      {0, -1},
      {1, 0},
      {0, 1},
  };

  void dfs(vector<vector<int>> &image, int r, int c, int color,
           int target_color) {
    if (r < 0 || r >= image.size() || c < 0 || c >= image[0].size() ||
        image[r][c] != target_color) {
      return;
    }
    image[r][c] = -1;
    for (auto dir : dirs) {
      int nr = r + dir[0], nc = c + dir[1];
      dfs(image, nr, nc, color, target_color);
    }
    image[r][c] = color;
  }

public:
  vector<vector<int>> floodFill(vector<vector<int>> &image, int sr, int sc,
                                int color) {
    dfs(image, sr, sc, color, image[sr][sc]);
    return image;
  }
};