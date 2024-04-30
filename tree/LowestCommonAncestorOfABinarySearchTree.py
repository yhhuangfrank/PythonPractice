# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # iteration
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stackA, stackB = [], []
        curr = root
        while curr.val != p.val:
            stackA.append(curr)
            if curr.val > p.val:
                curr = curr.left
            else:
                curr = curr.right
        curr = root
        while curr.val != q.val:
            stackB.append(curr)
            if curr.val > q.val:
                curr = curr.left
            else:
                curr = curr.right
        # compare two stacks
        while len(stackA) > len(stackB):
            popA = stackA.pop()
            if popA.val == q.val:
                return q
        while len(stackB) > len(stackA):
            popB = stackB.pop()
            if popB.val == p.val:
                return p
        # same stack size (tree depth)
        while len(stackA) > 1:
            popA, popB = stackA.pop(), stackB.pop()
            if popA.val == popB.val:
                return popA
        return stackA[0]
    
    
    def lowestCommonAncestorV2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if curr.val > p.val and curr.val > q.val:
                curr = curr.left
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right
            else:
                return curr # 一左一右