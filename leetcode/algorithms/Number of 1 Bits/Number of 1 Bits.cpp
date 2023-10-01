#include <cstdint>
using namespace std;

class Solution {
public:
  int hammingWeight(uint32_t n) {
    int res{};
    while (n > 0) {
      res += (n & 1);
      n >>= 1;
    }
    return res;
  }
};

class Solution2 {
public:
  int hammingWeight(uint32_t n) {
    int res{};
    for (int i = n; i != 0; i -= lowBit(i))
      res++;
    return res;
  }

  int lowBit(uint32_t x) { return x & -x; }
};