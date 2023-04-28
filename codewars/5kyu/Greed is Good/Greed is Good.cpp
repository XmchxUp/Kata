#include <vector>

int score(const std::vector<int> &dice) {
  int res = 0;
  int cnts[7] = {0};
  for (int i = 0; i < 6; i++) {
    cnts[dice[i]]++;
  }

  for (int i = 1; i <= 6; i++) {
    while (cnts[i] >= 3) {
      if (i == 1) {
        res += 1000;
      } else {
        res += i * 100;
      }
      cnts[i] -= 3;
    }
    if (cnts[i] > 0) {
      if (i == 1) {
        res += 100 * cnts[i];
      } else if (i == 5) {
        res += 50 * cnts[i];
      }
    }
  }
  return res;
}

int main() {
  std::vector<int> t{2, 3, 4, 6, 2};
  score(t);
  return 0;
}