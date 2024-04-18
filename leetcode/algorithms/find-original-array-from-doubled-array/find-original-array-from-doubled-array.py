from collections import deque


class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        if len(changed) % 2 != 0:
            return []

        q = deque()
        res = []
        changed.sort()
        for e in changed:
            if q:
                if q[0] < e:
                    return []
                if e == q[0]:
                    q.popleft()
                    continue
            res.append(e)
            q.append(e * 2)

        return [] if q else res
