# Given an m x n grid of characters board and a string word,
# return true if word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once.
from typing import List


class Solution:
    # O(m * n * 4^(len(word)))
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(r, c, pos):
            if (min(r, c) < 0 or r == ROWS or c == COLS
                    or board[r][c] != word[pos] or visited[r][c]):
                return False
            if board[r][c] == word[pos] and pos == len(word) - 1:
                return True

            visited[r][c] = True
            res = (
                dfs(r + 1, c, pos + 1) or
                dfs(r, c + 1, pos + 1) or
                dfs(r - 1, c, pos + 1) or
                dfs(r, c - 1, pos + 1)
            )
            visited[r][c] = False
            return res

        ROWS, COLS = len(board), len(board[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        for row in range(ROWS):
            for col in range(COLS):
                # 從 0 開始找 word 上的 char
                if dfs(row, col, 0):
                    return True
        return False


sol = Solution()
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
print(sol.exist(board, "ABCCED"))
print(sol.exist(board, "ABCD"))
print(sol.exist(board, "ASADE"))
