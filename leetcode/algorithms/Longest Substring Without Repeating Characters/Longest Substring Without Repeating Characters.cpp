#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
  int lengthOfLongestSubstring(string s) {
    if (s.size() == 0) {
      return 0;
    }
    unordered_map<char, int> cnts{};
    int i = 0, j = 0;
    int n = s.size();
    int res = 0;
    while (i < n) {
      while (j <= i && cnts[s[i]] > 0) {
        cnts[s[j]]--;
        j++;
      }
      cnts[s[i]]++;
      i++;
      res = max(res, i - j);
    }
    return res;
  }
};