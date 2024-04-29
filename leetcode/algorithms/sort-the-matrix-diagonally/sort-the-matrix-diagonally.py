from collections import defaultdict


class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        d = defaultdict(list)
        m, n = len(mat), len(mat[0])
        for i in range(0, m):
            for j in range(0, n):
                d[i - j].append(mat[i][j])

        for v in d.values():
            v.sort()

        for i in range(0, m):
            for j in range(0, n):
                mat[i][j] = d[i - j].pop(0)

        return mat
