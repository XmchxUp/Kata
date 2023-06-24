#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
private:
  bool is_only_numeric(const std::string str) {
    for (char c : str) {
      if (std::isalpha(c)) {
        return false;
      }
    }
    return true;
  }

public:
  int maximumValue(vector<string> &strs) {
    int res = 0;
    for (auto &s : strs) {
      if (is_only_numeric(s)) {
        res = std::max(res, std::stoi(s));
      } else {
        res = std::max(res, (int)s.size());
      }
    }
    return res;
  }
};