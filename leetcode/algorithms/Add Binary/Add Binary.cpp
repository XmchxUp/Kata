#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
  string addBinary(string a, string b) {
    string res{};
    int i = a.size() - 1, j = b.size() - 1;
    int sum = 0, carry = 0;
    while (i >= 0 || j >= 0) {
      if (i >= 0) {
        sum += (a[i] - '0');
        i--;
      }
      if (j >= 0) {
        sum += (b[j] - '0');
        j--;
      }
      res.push_back((sum % 2) + '0');
      sum /= 2;
    }
    if (sum > 0) {
      res.push_back(sum + '0');
    }
    std::reverse(res.begin(), res.end());
    return res;
  }
};