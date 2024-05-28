# You are given a network of n nodes, labeled from 1 to n. You are also given times,
# a list of travel times as directed edges times[i] = (ui, vi, wi),
# where ui is the source node, vi is the target node,
# and wi is the time it takes for a signal to travel from source to target.
#
# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal.
# If it is impossible for all the n nodes to receive the signal, return -1.
# Example 1:
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
#
# Example 2:
# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1
#
# Example 3:
# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1
import heapq
from typing import List


class Solution:
    # 應用 Dijkstra's algorithm
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        for src, dst, w in times:
            adj[src].append((dst, w))

        shortest = {}
        minHeap = [(0, k)]
        while minHeap:
            w1, node1 = heapq.heappop(minHeap)
            if node1 in shortest:
                continue
            shortest[node1] = w1
            if len(shortest) == n:  # 小優化，提早 return
                return max(shortest.values())
            for node2, w2 in adj[node1]:
                if node2 not in shortest:
                    heapq.heappush(minHeap, (w1 + w2, node2))
        return max(shortest.values()) if len(shortest) == n else -1


sol = Solution()
print(sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
print(sol.networkDelayTime([[1, 2, 1]], n=2, k=1))
print(sol.networkDelayTime([[1, 2, 1]], n=2, k=2))
