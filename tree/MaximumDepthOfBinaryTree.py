from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # dfs
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0
            return max(1 + dfs(node.left), 1 + dfs(node.right))

        return dfs(root)

    # bfs
    def maxDepthByBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque()
        q.append(root)
        lvl = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lvl += 1
        return lvl

    # iterative DFS
    def maxDepthByIteration(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = []
        maxD = 0
        stack.append((root, 1))
        while stack:
            node, depth = stack.pop()
            maxD = max(maxD, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return maxD
