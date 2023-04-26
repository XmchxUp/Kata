#include <iostream>
#include <vector>

void helper(std::vector<std::vector<int>> &res, std::size_t len) {
  if (len == 0) {
    return;
  }
  for (size_t i = 1; i < len; i++) {
    res[len - 1].emplace_back(1);
  }
  helper(res, len - 1);
}

std::vector<std::vector<int>> pyramid(std::size_t n) {
  // your code here
  std::vector<std::vector<int>> res{n, std::vector<int>{1}};
  helper(res, n);
  return res;
}

int main() { pyramid(1); }