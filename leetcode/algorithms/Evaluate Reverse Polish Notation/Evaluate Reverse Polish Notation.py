from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        :type tokens: List[str]
        :rtype: int
        """
        ar_set = set(["+", "-", "*", "/"])
        num_st = []
        ar_st = []
        for token in tokens:
            if token in ar_set:
                ar_st.append(token)
            else:
                num_st.append(int(token))

            while len(ar_st) > 0:
                ar = ar_st.pop()

                assert len(num_st) >= 2

                num2 = num_st.pop()
                num1 = num_st.pop()
                if ar == "+":
                    num_st.append(num1 + num2)
                elif ar == "-":
                    num_st.append(num1 - num2)
                elif ar == "/":
                    num_st.append(int(num1 / num2))
                elif ar == "*":
                    num_st.append(num1 * num2)
                else:
                    raise ValueError()
        assert len(num_st) == 1
        return num_st[0]


s = Solution()
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

print(s.evalRPN(["4", "13", "5", "/", "+"]))
