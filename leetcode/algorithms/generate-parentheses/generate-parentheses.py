from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(cur_s: str, open_cnt: int, close_cnt: int):
            if len(cur_s) == n * 2:
                res.append(cur_s)
                return

            if open_cnt < n:
                helper(cur_s + "(", open_cnt + 1, close_cnt)

            if close_cnt < open_cnt:
                helper(cur_s + ")", open_cnt, close_cnt + 1)

        helper("", 0, 0)

        return res
