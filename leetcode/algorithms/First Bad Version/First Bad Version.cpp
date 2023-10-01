// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
  int firstBadVersion(int n) {
    int lo = 1, hi = n;
    while (lo < hi) {
      int mid = ((hi - lo) >> 1) + lo;
      if (isBadVersion(mid)) {
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }
    return lo;
  }
};