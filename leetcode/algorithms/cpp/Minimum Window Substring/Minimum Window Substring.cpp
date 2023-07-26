#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
  string minWindow(string s, string t) {
    unordered_map<char, int> mt{}, ms{};
    for (char c : t) {
      mt[c]++;
    }

    string res{};
    int i = 0, j = 0;
    int n = s.size();
    int m = t.size();

    int count = 0;
    while (j < n) {
      ms[s[j]]++;

      if (ms[s[j]] <= mt[s[j]]) {
        count++;
      }

      while (i <= j && ms[s[i]] > mt[s[i]]) {
        ms[s[i]]--;
        i++;
      }

      if (count == m) {
        if (res.size() == 0 || j - i + 1 < res.size()) {
          res = s.substr(i, j - i + 1);
        }
      }
      j++;
    }
    return res;
  }
};

int main() {
  Solution().minWindow("ADOBECODEBANC", "ABC");
  return 0;
}