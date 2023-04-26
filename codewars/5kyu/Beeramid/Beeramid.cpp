#include <iostream>

// Returns number of complete beeramid levels
int beeramid(int bonus, double price) {
  // 9 2
  // 9 - 2 * 1 = 7
  // 1 4 9 16
  int level = 1;
  double money = bonus;
  while (money >= price * (level * level)) {
    money -= price * level * level;
    level++;
  }
  level--;
  return level;
}

// 21 1.5
// 21-1.5=19.5 1
// 19.5-6=13.5 4
// 13.5-13.5   4
int main() {
  std::cout << beeramid(9, 2) << std::endl;
  return 0;
}