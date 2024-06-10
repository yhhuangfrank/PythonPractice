# Given an m x n matrix, return all elements of the matrix in spiral order.
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        res = []
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1
        if r == 0:  # 只有一行
            return [matrix[i][0] for i in range(len(matrix))]
        if b == 0:  # 只有一列
            return list(matrix[0])

        def addToResult(row, col):
            if (row, col) not in visited:
                visited.add((row, col))
                res.append(matrix[row][col])

        while l <= r and t <= b:
            # top-left -> top-right
            for i in range(r - l + 1):  # i 表示 offset
                addToResult(t, l + i)
            # top-right -> bottom-right
            for i in range(b - t + 1):
                addToResult(t + i, r)
            # bottom-right -> bottom-left
            for i in range(r - l + 1):
                addToResult(b, r - i)
            # bottom-left -> top-left
            for i in range(b - t + 1):
                addToResult(b - i, l)
            # 縮小 matrix 範圍
            l += 1
            r -= 1
            t += 1
            b -= 1
        return res


sol = Solution()
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(sol.spiralOrder(matrix1))
print(sol.spiralOrder(matrix2))
