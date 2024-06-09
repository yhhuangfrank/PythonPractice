# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
#
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
from typing import List


class Solution:
    # 使用額外的 matrix 紀錄
    def rotate(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        temp = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            row = matrix[r]
            for c in range(COLS):
                temp[c][ROWS - 1 - r] = row[c]

        for r in range(ROWS):
            for c in range(COLS):
                matrix[r][c] = temp[r][c]

    # 使用額外的 matrix 紀錄
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            top, bottom = l, r
            for i in range(r - l):  # offset
                # save top-left value
                temp = matrix[top][l + i]
                # move bottom-left to top-left
                matrix[top][l + i] = matrix[bottom - i][l]
                # move bottom-right to bottom-left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                # move top-right to bottom-right
                matrix[bottom][r - i] = matrix[top + i][r]
                # move temp value to top-right
                matrix[top + i][r] = temp
            l += 1
            r -= 1


sol = Solution()
arr1 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
sol.rotate(arr1)
print(arr1)
