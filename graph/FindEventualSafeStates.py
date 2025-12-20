from collections import defaultdict, deque
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        sol1 = self.solution1(graph)
        print(f'solution1: {sol1}')
        sol2 = self.solution2(graph)
        print(f'solution2: {sol2}')
        return sol2

    # DFS, O(V + E) time, O(V) space
    def solution1(self, graph: List[List[int]]) -> List[int]:
        # 0: not access yet, 1: accessing, 2: is safe (no cycle)
        n = len(graph)
        node_state = {i: 0 for i in range(n)}

        def dfs(i):
            if node_state[i] == 1:
                return False
            if node_state[i] == 2:
                return True
            node_state[i] = 1
            for neighbor in graph[i]:
                if not dfs(neighbor):
                    return False
            node_state[i] = 2
            return True

        for i in range(n):
            dfs(i)
        res = []
        for i in range(n):
            if node_state[i] == 2:
                res.append(i)
        return res

    # Kahn's Algorithm, 建立 reverse_graph, O(V + E) time, O(V + E) space
    def solution2(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = defaultdict(list)
        out_degree = [0] * n # 原先的圖中有連接到多少鄰居
        for src, neighbors in enumerate(graph):
            for dst in neighbors:
                reverse_graph[dst].append(src)
            out_degree[src] = len(neighbors)

        # process every node whose out_degree is zero
        q = deque() # 儲存每個安全節點
        for node, degree in enumerate(out_degree):
            if degree == 0:  # terminal node
                q.append(node)
        while q:
            node = q.popleft()
            for prev_node in reverse_graph[node]:
                out_degree[prev_node] -= 1
                if out_degree[prev_node] == 0:
                    # 原圖中出度為 0 的節點也安全了
                    q.append(prev_node)
        # all out_degree = 0 are safe nodes
        res = []
        for node, degree in enumerate(out_degree):
            if degree == 0:
                res.append(node)
        return res

# Example 1:
# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]
# Explanation: The given graph is shown above.
# Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
# Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
#
# Example 2:
# Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
# Output: [4]
# Explanation:
# Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.
sol = Solution()
print(sol.eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []])) # [2,4,5,6]
print(sol.eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]])) # [4]