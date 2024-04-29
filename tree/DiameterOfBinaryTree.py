# Given the root of a binary tree, return the length of the diameter of the tree.
#
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
#
# The length of a path between two nodes is represented by the number of edges between them.
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(node):
            if not node.left and not node.right:
                return 0
            leftLen = 0
            rightLen = 0
            if node.left:
                leftLen = 1 + dfs(node.left)
            if node.right:
                rightLen = 1 + dfs(node.right)
            currLen = leftLen + rightLen
            res[0] = max(res[0], currLen)
            return max(leftLen, rightLen)

        if not root:
            return 0
        dfs(root)
        return res[0]
