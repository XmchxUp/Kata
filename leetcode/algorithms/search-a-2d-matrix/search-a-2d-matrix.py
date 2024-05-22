class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1

        while i < m and j >= 0:
            cmp = matrix[i][j] - target
            if cmp == 0:
                return True
            elif cmp < 0:
                i += 1
            else:
                j -= 1

        return False
