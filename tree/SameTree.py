# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(m + n) time
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # bfs
    def isSameTreeV2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append([p, q])
        while queue:
            size = len(queue)
            for _ in range(size):
                pair = queue.popleft()
                l, r = pair[0], pair[1]
                if (not l and r) or (l and not r) or (l and r and l.val != r.val):
                    return False
                if l and r:
                    queue.append([l.left, r.left])
                    queue.append([l.right, r.right])
        return True
