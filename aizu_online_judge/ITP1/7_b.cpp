#include <iostream>

int main() {
  int n, x;

  while (true) {
    std::cin >> n >> x;
    if (n == 0 && x == 0) {
      break;
    }
    int cnt = 0;
    for (int i = 1; i <= n; i++) {
      for (int j = i + 1; j <= n; j++) {
        for (int k = j + 1; k <= n; k++) {
          if (i + j + k == x) {
            cnt++;
          }
        }
      }
    }
    std::cout << cnt << std::endl;
  }
  return 0;
}