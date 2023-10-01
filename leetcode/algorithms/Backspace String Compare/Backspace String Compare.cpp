#include <stack>
#include <string>
using namespace std;

class Solution {
private:
  void countInfo(stack<char> &st, string &s) {
    for (char c : s) {
      if (c == '#' && !st.empty()) {
        st.pop();
      } else if (c != '#') {
        st.push(c);
      }
    }
  }

public:
  bool backspaceCompare(string s, string t) {
    stack<char> s1{}, s2{};
    countInfo(s1, s);
    countInfo(s2, t);
    return s1 == s2;
  }
};

class Solution2 {
private:
  string build(string &s) {
    int i = 0, j = 0;
    string res{s};
    while (j < s.size()) {
      if (s[j] == '#') {
        if (i > 0) {
          i--;
        }
      } else {
        res[i] = s[j];
        i++;
      }
      j++;
    }
    return res.substr(0, i);
  }

public:
  bool backspaceCompare(string s, string t) { return build(s) == build(t); }
};