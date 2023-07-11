#include <string>
#include <unordered_set>
using namespace std;

class Solution {
private:
  unordered_set<char> vs_{'a', 'e', 'i', 'o', 'u'};
  bool is_vowels(char c) { return vs_.count(std::tolower(c)) > 0; }

public:
  string reverseVowels(string s) {
    int i = 0, j = s.size() - 1;
    while (i < j) {
      bool f1 = is_vowels(s[i]);
      bool f2 = is_vowels(s[j]);
      if (f1 && f2) {
        char c = s[i];
        s[i] = s[j];
        s[j] = c;
        i++;
        j--;
      } else if (f1) {
        j--;
      } else {
        i++;
      }
    }
    return s;
  }
};