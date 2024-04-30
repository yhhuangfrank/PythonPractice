# Given a binary tree root, a node X in the tree is named good
# if in the path from root to X there are no nodes with a value greater than X.
#
# Return the number of good nodes in the binary tree.

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(n)
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        self.dfs(root, root.val, res)
        return res[0]

    def dfs(self, node, currMax, res):
        if not node:
            return
        newMax = currMax
        if node.val >= currMax:
            newMax = node.val
            res[0] += 1

        self.dfs(node.left, newMax, res)
        self.dfs(node.right, newMax, res)


    # 另外一種 dfs
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, currMax):
            if not node:
                return 0  # 返回數量
            res = 1 if node.val >= currMax else 0
            currMax = max(currMax, node.val)
            res += dfs(node.left, currMax)
            res += dfs(node.right, currMax)
            return res

        return dfs(root, root.val)

