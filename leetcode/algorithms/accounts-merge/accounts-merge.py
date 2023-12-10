from typing import List
from collections import defaultdict


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in uf.parent:
                    uf.parent[email] = email
                uf.union(account[1], email)
                email_to_name[email] = name

        email_to_ids = defaultdict(list)
        for email in uf.parent:
            email_to_ids[uf.find(email)].append(email)

        return [[email_to_name[v[0]]] + sorted(v) for v in email_to_ids.values()]
