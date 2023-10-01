class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m = dict()
        for s in strs:
            t = "".join(sorted(s))
            if t not in m:
                m[t] = []
            m[t].append(s)

        res = []
        for v in m.values():
            res.append(v)
        return res
