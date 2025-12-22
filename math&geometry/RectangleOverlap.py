# Example 1:
# Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# Output: true
#
# Example 2:
# Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# Output: false
#
# Example 3:
# Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
# Output: false
from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x_index = [(rec1[0], rec1[2]), (rec2[0], rec2[2])]
        y_index = [(rec1[1], rec1[3]), (rec2[1], rec2[3])]

        # 有重疊，表示 x 線段重疊，且 y 線段重疊
        x_index.sort(key=lambda x: x[0])
        y_index.sort(key=lambda y: y[0])

        (x1, x2), (x3, x4) = x_index
        (y1, y2), (y3, y4) = y_index

        return x3 < x2 and y3 < y2


sol = Solution()
print(sol.isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3]))
print(sol.isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1]))
print(sol.isRectangleOverlap([0, 0, 1, 1], [2, 2, 3, 3]))
