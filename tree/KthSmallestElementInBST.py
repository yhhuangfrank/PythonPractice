# Given the root of a binary search tree,
# and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
#
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursion
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in-order traversal
        def dfs(node, lst):
            if not node:
                return
            if node.left:
                dfs(node.left, lst)
            lst.append(node.val)
            if node.right:
                dfs(node.right, lst)

        lst = []
        dfs(root, lst)
        return lst[k - 1]

    # iteration
    def kthSmallestByIteration(self, root: Optional[TreeNode], k: int) -> int:
        lst, stack = [], []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                pop = stack.pop()
                lst.append(pop.val)
                node = pop.right
        return lst[k - 1]

