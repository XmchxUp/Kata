
class Solution {
public:
  bool isPalindromeV2(int x) {
    if (x < 0 || (x % 10 == 0 && x != 0)) {
      return false;
    }

    int y = 0;
    while (y < x) {
      y = y * 10 + x % 10;
      x /= 10;
    }
    return x == y || x == y / 10;
  }
  bool isPalindrome(int x) {
    if (x < 0) {
      return false;
    }

    long y = 0;
    int curr = x;
    while (curr > 0) {
      y = y * 10 + (curr % 10);
      curr /= 10;
    }
    return y == x;
  }
};