# There are n cities connected by some number of flights.
# You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that
# there is a flight from city fromi to city toi with cost pricei.
#
# You are also given three integers src, dst, and k,
# return the cheapest price from src to dst with at most k stops.
# If there is no such route, return -1.
#
# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
# Output: 700
# Explanation:
# The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
# Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph is shown above.
# The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
from collections import deque
from typing import List


class Solution:
    # brute force
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: [] for i in range(n)}
        for start, end, price in flights:
            adj[start].append((end, price))

        minPrice = [float("inf")]
        visited = set()

        def dfs(v, curr, currCount):
            if v in visited:
                return
            if v == dst and currCount <= k + 1:
                minPrice[0] = min(minPrice[0], curr)
                return
            visited.add(v)
            for neighbor, p in adj[v]:
                dfs(neighbor, p + curr, currCount + 1)
            visited.remove(v)

        dfs(src, 0, 0)
        return minPrice[0] if minPrice[0] != float("inf") else -1

    # bfs, O(E * K) time
    def findCheapestPriceV2(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: [] for i in range(n)}
        for s, d, p in flights:
            adj[s].append((d, p))

        minCost = [float("inf")] * n
        minCost[src] = 0
        lvl = 0
        q = deque()
        q.append((src, 0))

        while q and lvl < k + 1:
            size = len(q)
            temp = list(minCost)
            for _ in range(size):
                d, _ = q.popleft()
                for neighbor, p2 in adj[d]:
                    if minCost[d] == float("inf"):
                        continue
                    if minCost[d] + p2 < temp[neighbor]:
                        temp[neighbor] = minCost[d] + p2
                        q.append((neighbor, p2))  # 比原有的小才加入 q
            minCost = temp
            lvl += 1

        return minCost[dst] if minCost[dst] != float("inf") else -1

    # V2 的簡單版本，核心概念相同 (Bellman-Ford algorithm)
    def findCheapestPriceV3(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        minCost = [float("inf")] * n
        minCost[src] = 0

        for _ in range(k + 1):
            temp = list(minCost)
            for s, d, p in flights:
                if minCost[s] == float("inf"):
                    continue
                if minCost[s] + p < temp[d]:
                    temp[d] = minCost[s] + p
            minCost = temp

        return minCost[dst] if minCost[dst] != float("inf") else -1


sol = Solution()
flights1 = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
flights2 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
flights3 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
# print(sol.findCheapestPrice(n=4, flights=flights1, src=0, dst=3, k=1))
# print(sol.findCheapestPrice(n=3, flights=flights2, src=0, dst=2, k=1))
# print(sol.findCheapestPrice(n=3, flights=flights3, src=0, dst=2, k=0))
print(sol.findCheapestPriceV2(n=4, flights=flights1, src=0, dst=3, k=1))
print(sol.findCheapestPriceV2(n=3, flights=flights2, src=0, dst=2, k=1))
print(sol.findCheapestPriceV2(n=3, flights=flights3, src=0, dst=2, k=0))
print("=================================================================")
print(sol.findCheapestPriceV3(n=4, flights=flights1, src=0, dst=3, k=1))
print(sol.findCheapestPriceV3(n=3, flights=flights2, src=0, dst=2, k=1))
print(sol.findCheapestPriceV3(n=3, flights=flights3, src=0, dst=2, k=0))
