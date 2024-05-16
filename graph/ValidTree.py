# Input:
# n = 5
# edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Output:
# true

# Input:
# n = 5
# edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
#
# Output:
# false


from typing import List


class UnionFind:
    def __init__(self, numNodes):
        self.parent = {}
        self.rank = {}
        for i in range(numNodes):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, node):
        p = self.parent[node]
        while p != self.parent[node]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return False
        r1, r2 = self.rank[p1], self.rank[p2]
        if r1 < r2:
            self.parent[p1] = p2
        elif r1 > r2:
            self.parent[p2] = p1
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        return True


class Solution:
    # 使用 UnionFind 解法
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) < n - 1:  # 至少要 n - 1 個 edges (每個節點才會相連)
            return False
        # 判斷 graph 是否有 cycle
        uf = UnionFind(n)
        for n1, n2 in edges:
            if not uf.union(n1, n2):
                return False
        return True

    # DFS 解法
    def validTreeV2(self, n: int, edges: List[List[int]]) -> bool:
        nodeMap, visited = {i: [] for i in range(n)}, set()

        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for neigh in nodeMap[node]:
                if neigh == prev:  # 與 prev 相同不用再次遍歷，否則誤判 cycle
                    continue
                if not dfs(neigh, node):
                    return False
            return True

        for n1, n2 in edges:
            nodeMap[n1].append(n2)
            nodeMap[n2].append(n1)
        # 節點數要相同，0 號節點的 prev 用 -1 (節點從 0 開始編號)
        return dfs(0, -1) and len(visited) == n


sol = Solution()
arr = [[0, 1], [0, 2], [0, 3], [1, 4]]
arr1 = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
num = 5
print(sol.validTree(num, arr))
print(sol.validTreeV2(num, arr))
print(sol.validTree(num, arr1))
print(sol.validTreeV2(num, arr1))
