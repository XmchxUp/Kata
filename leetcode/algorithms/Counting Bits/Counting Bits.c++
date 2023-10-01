#include <vector>
using namespace std;

/*
odd
  0 = 00  1 = 01
  2 = 10  3 = 11
  4 = 100 5 = 101
even
  2 = 10  4 = 100  8 = 1000
  3 = 11  6 = 110  12 = 1100
*/
class Solution {
public:
  vector<int> countBits(int n) {
    vector<int> cnts(n + 1, 0);
    for (int i = 1; i <= n; i++) {
      if (i % 2 == 0) {
        cnts[i] = cnts[i >> 1];
      } else {
        cnts[i] = cnts[i - 1] + 1;
      }
    }
    return cnts;
  }
};