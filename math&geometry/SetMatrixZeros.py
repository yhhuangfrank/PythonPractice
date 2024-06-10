# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
#
# You must do it in place.
#
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
from typing import List


class Solution:
    # O(mn) time, O(m+n) space
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for r in zero_rows:
            matrix[r] = [0] * COLS

        for i in range(ROWS):
            for j in range(COLS):
                if j in zero_cols:
                    matrix[i][j] = 0

    # O(1) memory
    def setZeroesV2(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        firstRowIsZero = False

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0  # mark this col
                    if i > 0:
                        matrix[i][0] = 0  # mark this row
                    else:
                        firstRowIsZero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        # handle first col and row
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        if firstRowIsZero:
            for c in range(COLS):
                matrix[0][c] = 0


sol = Solution()
matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
sol.setZeroes(matrix1)
sol.setZeroes(matrix2)
print(matrix1)
print(matrix2)
