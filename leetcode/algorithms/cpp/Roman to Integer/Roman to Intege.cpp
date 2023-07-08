#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
  int romanToInt(string s) {
    unordered_map<char, int> m = {{'I', 1},   {'V', 5},   {'X', 10},  {'L', 50},
                                  {'C', 100}, {'D', 500}, {'M', 1000}};
    bool isMinus = false;
    char prev = s[0];
    int val = 0;
    for (char c : s) {
      if (m[prev] < m[c]) {
        isMinus = true;
      } else {
        isMinus = false;
      }
      if (isMinus) {
        val = val + m[c] - m[prev] * 2;
      } else {
        val = val + m[c];
      }
      prev = c;
    }
    return val;
  }
};

int main() {
  Solution s;
  s.romanToInt("MCMXCIV");
  return 0;
}
