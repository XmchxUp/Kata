#include <string>

std::string alphabet_position(const std::string &text) {
  std::string res{};
  for (auto c : text) {
    if ('a' <= c && c <= 'z') {
      res.append(std::to_string(c - 'a' + 1) + " ");
    } else if ('A' <= c && c <= 'Z') {
      res.append(std::to_string(c - 'A' + 1) + " ");
    }
  }
  if (res.size()) {
    res.pop_back();
  }
  return res;
}