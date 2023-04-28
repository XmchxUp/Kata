#include <cmath>
#include <string>
bool narcissistic(int value) {
  // Code away
  if (value < 10) {
    return true;
  }
  int n = std::to_string(value).size();
  int tmp_val = value;
  int new_val = 0;
  while (tmp_val != 0) {

    new_val += pow(tmp_val % 10, 3);
    tmp_val /= 10;
  }
  return new_val == value;
}