#include <string>
#include <vector>
using namespace std;

class Solution {
public:
  string longestCommonPrefix(vector<string> &strs) {
    if (strs.size() == 0) {
      return "";
    }
    char cur = strs[0][0];
    string res = "";
    int n = strs[0].size();
    for (int i = 0; i < n; i++) {
      cur = strs[0][i];
      for (string str : strs) {
        if (str[i] != cur) {
          i = strs[0].size();
          break;
        }
      }
      if (i < n)
        res += cur;
    }
    return res;
  }
};