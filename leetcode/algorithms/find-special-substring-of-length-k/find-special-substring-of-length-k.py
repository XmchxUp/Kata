class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        cnt = 0
        for i, c in enumerate(s):
            cnt += 1
            if i == len(s) - 1 or c != s[i + 1]:
                if cnt == k:
                    return True
                cnt = 0
        return False
