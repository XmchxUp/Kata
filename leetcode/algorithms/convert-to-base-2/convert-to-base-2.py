class Solution(object):
    def baseNeg2(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return "0"
        res = ""
        while n != 0:
            if n % -2 == 0:
                res += "0"
            else:
                n -= 1
                res += "1"
            n //= -2
        return res[::-1]
