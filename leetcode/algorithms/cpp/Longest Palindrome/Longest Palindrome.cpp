#include <string>
#include <unordered_map>
using namespace std;
class Solution {
public:
  int longestPalindrome(string s) {
    std::unordered_map<char, int> m{};
    for (char c : s) {
      m[c]++;
    }
    int res = 0;
    bool hasOdd = false;
    for (auto p : m) {
      if (p.second % 2 == 0) {
        res += p.second;
      } else {
        hasOdd = true;
        if (p.second > 1) {
          res += (p.second - 1);
        }
      }
    }
    if (hasOdd) {
      return res + 1;
    } else {
      return res;
    }
  }
};