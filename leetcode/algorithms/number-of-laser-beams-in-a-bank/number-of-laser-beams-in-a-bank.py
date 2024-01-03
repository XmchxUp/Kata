from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        previous_cnt = 0
        total = 0
        for i in range(len(bank)):
            cnt = bank[i].count("1")
            if cnt > 0:
                total += previous_cnt * cnt
                previous_cnt = cnt
        return total