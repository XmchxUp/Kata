#include <cstdint>

class Solution {
public:
  /**
   * 分而治至，每16位 -> 8位 -> 4 -> 2 -> 1交换
   */
  uint32_t reverseBitsV2(uint32_t n) {
    n = (n >> 16) | (n << 16);
    n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8);
    n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4);
    n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2);
    n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1);
    return n;
  }

  uint32_t reverseBits(uint32_t n) {
    uint32_t res = 0;
    int i = 0;
    while (n > 0) {
      if (n % 2 == 1) {
        res = (res << 1) + 1;
      } else {
        res = res << 1;
      }
      n >>= 1;
      i++;
    }
    while (i < 32) {
      res = res << 1;
      i++;
    }
    return res;
  }
};