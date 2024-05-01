# Given two integer arrays preorder and inorder
# where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree,
# construct and return the binary tree.
#

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 解法一，分開出新陣列
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        return root

    # 解法二，使用 index
    def buildTreeV2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idxMap = {val: idx for idx, val in enumerate(inorder)} # 每個 val 為 unique

        def build(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            root = TreeNode(preorder[pre_left])
            idx = idxMap[root.val]
            left_len = idx - in_left
            right_len = in_right - idx
            root.left = build(pre_left + 1, pre_left + left_len, in_left, idx - 1)
            root.right = build(pre_right - right_len + 1, pre_right, idx + 1, in_right)
            return root

        n = len(preorder)
        return build(0, n - 1, 0, n - 1)