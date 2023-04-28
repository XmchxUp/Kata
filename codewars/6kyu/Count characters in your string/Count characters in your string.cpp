#include <map>
#include <string>

std::map<char, unsigned> count(const std::string &string) {
  std::map<char, unsigned> res{};
  for (const char &c : string) {
    res[c]++;
  }
  return res;
}
