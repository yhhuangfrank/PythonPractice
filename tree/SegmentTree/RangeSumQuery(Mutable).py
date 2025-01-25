from typing import List


class Node:
    def __init__(self, total, L, R):
        self.total = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R

class NumArray:

    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)
    
    def build(self, nums, l, r):
        if l == r:
            return Node(nums[l], l, r)
        root = Node(0, l, r)
        m = l + (r - l) // 2
        root.left = self.build(nums, l, m)
        root.right = self.build(nums, m + 1, r)
        root.total = root.left.total + root.right.total
        return root

    def update(self, index: int, val: int) -> None:

        def updateHelper(node, index, val):
            if node.L == node.R:
                node.total = val
                return
            m = node.L + (node.R - node.L) // 2
            if index > m:
                updateHelper(node.right, index, val)
            else:
                updateHelper(node.left, index, val)
            node.total = node.left.total + node.right.total
        
        updateHelper(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:

        def helper(node, L, R):
            if L == node.L and R == node.R:
                return node.total
            m = node.L + (node.R - node.L) // 2
            if L > m:
                return helper(node.right, L, R)
            elif R <= m:
                return helper(node.left, L, R)
            else:
                return (
                    helper(node.left, L, m) +
                    helper(node.right, m + 1, R)
                )
    
        return helper(self.root, left, right)


nums = [1, 3, 5]
numArray = NumArray(nums)
print(numArray.sumRange(0, 2)); # return 1 + 3 + 5 = 9
numArray.update(1, 2);  # nums = [1, 2, 5]
print(numArray.sumRange(0, 2));# return 1 + 2 + 5 = 8