#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
  vector<vector<string>> groupAnagrams(vector<string> &strs) {
    unordered_map<string, vector<string>> hash{};
    for (auto &s : strs) {
      auto nstr = s;
      std::sort(nstr.begin(), nstr.end());
      hash[nstr].push_back(s);
    }

    vector<vector<string>> res{};
    for (auto &e : hash) {
      res.push_back(e.second);
    }
    return res;
  }
};