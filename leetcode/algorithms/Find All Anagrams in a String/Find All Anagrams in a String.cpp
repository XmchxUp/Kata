#include <string>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> findAnagrams(string s, string p) {
    vector<int> res;

    int n = s.size();
    int m = p.size();

    vector<int> m1(26, 0);
    vector<int> m2(26, 0);
    for (char c : p) {
      m1[c - 'a']++;
    }

    // cbaebabacd
    // abc
    int i = 0, j = 0;
    while (j < n) {
      m2[s[j] - 'a']++;
      if (m1 == m2) {
        res.push_back(i);
        m2[s[i] - 'a']--;
        i++;
      }
      j++;
      while (j - i >= m) {
        m2[s[i] - 'a']--;
        i++;
      }
    }
    return res;
  }
};