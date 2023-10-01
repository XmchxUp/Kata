class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        c1, c2 = {}, {}
        for c in s:
            c1[c] = c1.get(c, 0) + 1
        for c in t:
            c2[c] = c2.get(c, 0) + 1
        return c1 == c2
