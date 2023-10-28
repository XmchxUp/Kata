class Solution:
    def countDigits(self, num: int) -> int:
        tmp_num = num
        res = 0
        while tmp_num > 0:
            if num % (tmp_num % 10) == 0:
                res += 1
            tmp_num //= 10
        return res
