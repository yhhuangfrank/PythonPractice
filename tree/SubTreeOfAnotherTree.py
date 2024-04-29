from typing import Optional


# 給定一 tree 和 subTree 的 root。判斷 subTree 是否為 tree 的子樹 (所有後代都須相同)
# 同一顆樹也被視為是一種 subTree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 找到 subtree 的 root
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
