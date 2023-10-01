class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check row
        for i in range(9):
            m = [False] * 9
            for j in range(9):
                if board[i][j] == ".":
                    continue
                idx = int(board[i][j]) - 1
                if m[idx]:
                    return False
                m[idx] = True
        # check col
        for j in range(9):
            m = [False] * 9
            for i in range(9):
                if board[i][j] == ".":
                    continue
                idx = int(board[i][j]) - 1
                if m[idx]:
                    return False
                m[idx] = True

        for i in range(3):
            for j in range(3):
                m = [False] * 9
                for x in range(3):
                    for y in range(3):
                        if board[x + i * 3][y + j * 3] == ".":
                            continue
                        idx = int(board[x + i * 3][y + j * 3]) - 1
                        if m[idx]:
                            return False
                        m[idx] = True
        return True
