from typing import List


# 找到一 graph 節點相連的 component 共有幾個
class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        self.numComponets = n
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, x):
        p = self.parent[x]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, x, y):
        p1, p2 = self.parent[x], self.parent[y]
        if p1 == p2:
            return False
        r1, r2 = self.rank[p1], self.rank[p2]
        if r1 < r2:
            self.parent[p1] = p2
        elif r2 < r1:
            self.parent[p2] = p1
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        self.numComponets -= 1
        return True

    def getNumComponets(self):
        return self.numComponets


class Solution:
    # 解法一 dfs
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodeMap = {i: [] for i in range(n)}
        visited = set()
        count = 0

        def dfs(node, prev):
            if node in visited:
                return
            visited.add(node)
            for neighbor in nodeMap[node]:
                if neighbor == prev:
                    continue
                dfs(neighbor, node)

        for n1, n2 in edges:
            nodeMap[n1].append(n2)
            nodeMap[n2].append(n1)

        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                count += 1
        return count

    # 解法二：Union Find
    def countComponentsV2(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for n1, n2 in edges:
            uf.union(n1, n2)
        return uf.getNumComponets()


sol = Solution()
arr1 = [[0, 1], [0, 2]]
arr2 = [[0, 1], [1, 2], [2, 3], [4, 5]]
print(sol.countComponents(3, arr1))
print(sol.countComponentsV2(3, arr1))
print(sol.countComponents(6, arr2))
print(sol.countComponentsV2(6, arr2))
