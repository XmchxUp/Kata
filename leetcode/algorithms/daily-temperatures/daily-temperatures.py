from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        max_st = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while len(max_st) > 0 and temperatures[max_st[-1]] < temperatures[i]:
                cur_idx = max_st.pop(-1)
                res[cur_idx] = i - cur_idx
            max_st.append(i)
        return res
