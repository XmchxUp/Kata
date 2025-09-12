# Created by Xmchx at 2025/09/12 09:02
# leetgo: dev
# https://leetcode.cn/problems/vowels-game-in-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set("aeiou")
        return any(c in vowels for c in s)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().doesAliceWin(s)
    print("\noutput:", serialize(ans, "boolean"))
