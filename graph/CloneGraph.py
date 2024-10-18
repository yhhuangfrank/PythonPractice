import collections
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    # DFS solution
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        table = {}

        def dfs(n):
            if str(n.val) in table:
                return table[str(n.val)]
            newNode = Node(n.val)
            table[str(n.val)] = newNode
            for neigh in n.neighbors:
                newNode.neighbors.append(dfs(neigh))
            return newNode

        return dfs(node)

    # BFS
    def cloneGraphByBFS(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        table = {}
        q = collections.deque()
        q.append(node)
        table[node] = Node(node.val)

        while q:
            size = len(q)
            for _ in range(size):
                pop = q.popleft()
                for neigh in pop.neighbors:
                    if neigh not in table:
                        q.append(neigh)
                        table[neigh] = Node(neigh.val)
                    table[pop].neighbors.append(table[neigh])

        return table[node]
