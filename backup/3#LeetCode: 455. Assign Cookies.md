# LeetCode: 455. Assign Cookies

将两个数组排序，从大到小遍历尽可能的满足Big小孩的需要。

```python
from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        i, j = len(g) - 1, len(s) - 1
        while i >= 0 and j >= 0:
            if s[j] >= g[i]:
                res += 1
                j -= 1
                i -= 1
            else:
                i -= 1
        return res
```

---

* Link: https://github.com/XmchxUp/Kata/issues/3
* Labels: `greedy`
* Creation Date: 2024-01-01T01:17:41Z
