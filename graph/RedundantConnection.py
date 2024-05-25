# 給定一 array，代表 graph 的 edges，問刪除哪個 edge 可讓 graph 不構成環
# 若有多個答案，回傳最後出現的 edge
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        for i in range(1, n + 1):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, x):
        p = self.parent[x]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return False
        r1, r2 = self.rank[p1], self.rank[p2]
        if r1 > r2:
            self.parent[p2] = p1
        elif r1 < r2:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        unionFind = UnionFind(len(edges))
        for n1, n2 in edges:
            if not unionFind.union(n1, n2):
                return [n1, n2]
        return [-1, -1]


sol = Solution()
print(sol.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
print(sol.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
