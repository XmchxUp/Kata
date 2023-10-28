from typing import List
from collections import deque


class Solution:
    """
    拓扑排序,DAG,检测入度为0的个数
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]

        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)

        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        cnt = 0
        while len(q) > 0:
            cNo = q.popleft()
            cnt += 1
            for c in adjacency[cNo]:
                indegrees[c] -= 1
                if indegrees[c] == 0:
                    q.append(c)
        return cnt == numCourses
