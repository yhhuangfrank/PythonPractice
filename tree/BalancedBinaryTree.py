# Given a binary tree, determine if it is height-balanced.
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # O(n ^ 2)
        def dfs(node):
            if not node:
                return 0
            # leaf node
            if not node.left and not node.right:
                return 1
            leftHeight = 1 + dfs(node.left)
            rightHeight = 1 + dfs(node.right)
            return max(leftHeight, rightHeight)

        if not root:
            return True
        if abs(dfs(root.left) - dfs(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    # O(n) time
    def isBalancedV2(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            if (abs(leftHeight - rightHeight) > 1
                    or leftHeight == -1
                    or rightHeight == -1):
                return -1
            return 1 + max(leftHeight, rightHeight)

        return dfs(root) != -1

    # O(n) 返回 subtree 是否平衡與其高度
    def isBalancedV3(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, 0]  # (subtree is balanced, subtree height)
            left = dfs(node.left)
            right = dfs(node.right)
            balanced = (left[0] and right[0]
                        and abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
