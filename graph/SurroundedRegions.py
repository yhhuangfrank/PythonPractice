# Given an m x n matrix board containing 'X' and 'O',
# capture all regions that are 4-directionally surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.

from typing import List


class Solution:
    # brute force dfs
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited = [[False] * COLS for _ in range(ROWS)]

        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS:
                return False
            if visited[r][c] or board[r][c] == "X":
                return True

            visited[r][c] = True
            res = (
                dfs(r + 1, c) and
                dfs(r, c + 1) and
                dfs(r - 1, c) and
                dfs(r, c - 1)
            )
            visited[r][c] = False
            return res

        for row in range(ROWS):
            for col in range(COLS):
                if min(row, col) == 0 or row == ROWS - 1 or col == COLS - 1:
                    continue
                if dfs(row, col):
                    board[row][col] = "X"

    # dfs
    def solveV2(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        temp = "T"
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS
                    or board[r][c] != "O"):
                return
            board[r][c] = temp
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # dfs from boarder and change to temp
        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS - 1)
        for col in range(COLS):
            dfs(0, col)
            dfs(ROWS - 1, col)

        # change O -> X,  change T -> O
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == temp:
                    board[row][col] = "O"


sol = Solution()
board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]
board2 = board.copy()
sol.solve(board)
sol.solveV2(board2)
print(board)
print(board2)
