from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        table = [-1] * n  # 每一(index,元素)代表在 (index, 元素值) 位置有 queen
        res = []
        cols = set()
        posDiagnol = set()  # 紀錄正斜率有哪些
        negDiagnol = set()  # 紀錄負斜率有哪些

        def dfs(r):
            if r == n:
                recordBoard()
                return
            for c in range(n):
                if c in cols or (r + c) in posDiagnol or (r - c) in negDiagnol:
                    continue
                table[r] = c
                cols.add(c)
                posDiagnol.add(r + c)
                negDiagnol.add(r - c)
                dfs(r + 1)
                table[r] = -1
                cols.remove(c)
                posDiagnol.remove(r + c)
                negDiagnol.remove(r - c)

        def recordBoard():
            lst = []
            cur = ""
            for col in table:
                for _ in range(col):
                    cur += "."
                cur += "Q"
                for _ in range(n - col - 1):
                    cur += "."
                lst.append(cur)
                cur = ""
            res.append(lst)

        dfs(0)
        return res


sol = Solution()
print(sol.solveNQueens(4))
print(sol.solveNQueens(1))
print(len(sol.solveNQueens(8)))
print(len(sol.solveNQueens(9)))
