# 給定一二維座標平面，約定任兩點 (x1, y1), (x2, y2) 距離為 abs(x1 - x2) + abs(y1 - y2)
# 給予 points list，找出將所有點連線皆 connected (彼此可以互相沿著路線走到) 的總共最小花費 (距離) 為何？
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18
import heapq
from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
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
        p1, p2 = self.find(x), self.find(y)
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
        return True


class Solution:
    # Prim's algorithm
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i: [] for i in range(len(points))}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]
                dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        minHeap = [(0, 0)]  # (dist, node), 初始放入 0 號節點到自己的距離為 0
        mstCost = 0
        visited = set()
        while minHeap:
            dist1, node1 = heapq.heappop(minHeap)
            if node1 in visited:
                continue
            mstCost += dist1
            visited.add(node1)
            if len(visited) == len(points):
                return mstCost
            for dist2, node2 in adj[node1]:
                if node2 not in visited:
                    heapq.heappush(minHeap, (dist2, node2))
        return mstCost

    # Kruskal's algorithm
    def minCostConnectPointsV2(self, points: List[List[int]]) -> int:
        minHeap = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]
                dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                heapq.heappush(minHeap, (dist, i, j))

        n = len(points)
        components = n
        uf = UnionFind(n)
        mstCount = 0

        while components > 1 and minHeap:
            dist, n1, n2 = heapq.heappop(minHeap)
            if uf.union(n1, n2):
                mstCount += dist
                components -= 1
        return mstCount


sol = Solution()
arr1 = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
arr2 = [[3, 12], [-2, 5], [-4, 1]]
print(sol.minCostConnectPoints(arr1))
print(sol.minCostConnectPoints(arr2))
print(sol.minCostConnectPointsV2(arr1))
print(sol.minCostConnectPointsV2(arr2))
