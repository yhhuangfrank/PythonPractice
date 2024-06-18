# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
from typing import List


class Solution:
    # O(n^2) time
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        # preparation
        rowSets, colSets = [], []
        for r in range(ROWS):
            rowSets.append(set())
        for c in range(COLS):
            colSets.append(set())
        subBoxes = []
        for _ in range(3):
            lst = []
            for _ in range(3):
                lst.append(set())
            subBoxes.append(lst)

        for r in range(ROWS):
            for c in range(COLS):
                val = board[r][c]
                if val == ".":
                    continue
                # check rows
                if val in rowSets[r]:
                    return False
                rowSets[r].add(val)
                # check cols
                if val in colSets[c]:
                    return False
                colSets[c].add(val)
                # check sub-box
                if val in subBoxes[r // 3][c // 3]:
                    return False
                subBoxes[r // 3][c // 3].add(val)
        return True


sol = Solution()
grid1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
grid2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
print(sol.isValidSudoku(grid1))
print(sol.isValidSudoku(grid2))
