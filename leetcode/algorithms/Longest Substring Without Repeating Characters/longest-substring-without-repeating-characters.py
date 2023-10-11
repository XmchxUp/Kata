class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lo, hi = 0, 0
        cnts = dict()
        res = 0
        while hi < len(s):
            if s[hi] not in cnts:
                cnts[s[hi]] = 0
            cnts[s[hi]] += 1
            if cnts[s[hi]] > 1:
                while cnts[s[hi]] > 1:
                    cnts[s[lo]] -= 1
                    lo += 1
            hi += 1
            res = max(res, hi - lo)
        return res
