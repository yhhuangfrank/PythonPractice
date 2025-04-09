class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [-1] * n # index 表示所在列, 元素值代表所在行

        def isValid(i):
            for r in range(i):
                if board[r] == board[i]: return False
                if abs(r - i) == abs(board[r] - board[i]): return False
            return True
        
        def backtrack(i):
            if i == n:
                return 1
            res = 0
            for j in range(n):
                board[i] = j
                if isValid(i):
                    res += backtrack(i + 1)
                board[i] = -1
            return res

        return backtrack(0)

sol = Solution()
print(sol.totalNQueens(4))
print(sol.totalNQueens(1))
print(sol.totalNQueens(8))
