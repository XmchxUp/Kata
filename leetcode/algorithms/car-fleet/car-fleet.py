from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        times = [0] * n

        for i, (pos, sp) in enumerate(sorted(zip(position, speed))):
            times[i] = (target - pos) / sp

        st = []
        for t in times:
            while st and t >= st[-1]:
                st.pop()
            st.append(t)

        return len(st)
