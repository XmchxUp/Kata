#include <iostream>

int main() {
  int m = 0, f = 0, r = 0;
  char grade;
  while (1) {
    std::cin >> m >> f >> r;
    if (m == -1 && f == -1 && r == -1) {
      break;
    }
    int total = m + f;
    if (m == -1 or f == -1) {
      grade = 'F';
    } else if (total >= 80) {
      grade = 'A';
    } else if (total >= 65) {
      grade = 'B';
    } else if (total >= 50 or r >= 50) {
      grade = 'C';
    } else if (total >= 30) {
      grade = 'D';
    } else {
      grade = 'F';
    }
    std::cout << grade << std::endl;
  }
  return 0;
}