from typing import List

class Solution:
    # brute force, O(m*n*4^(m*n))
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        def dfs(i, j, prev):
            if min(i, j) < 0 or i == ROWS or j == COLS or matrix[i][j] <= prev:
                return 0
            cur = matrix[i][j]
            return 1 + max(
                dfs(i + 1, j, cur),
                dfs(i, j + 1, cur),
                dfs(i - 1, j, cur),
                dfs(i, j - 1, cur),
            )
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c, float("-inf")))
        return res

    # memoization, O(m * n) time
    def longestIncreasingPathV2(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}

        def dfs(i, j, prev):
            if min(i, j) < 0 or i == ROWS or j == COLS or matrix[i][j] <= prev:
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            cur = matrix[i][j]
            cache[(i, j)] = 1 + max(
                dfs(i + 1, j, cur),
                dfs(i, j + 1, cur),
                dfs(i - 1, j, cur),
                dfs(i, j - 1, cur),
            )
            return cache[(i, j)]
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c, float("-inf")))
        return res

sol = Solution()
# Input: matrix = [[5,5,3],[2,3,6],[1,1,1]]
# Output: 4
matrix = [[5,5,3],[2,3,6],[1,1,1]]
print(sol.longestIncreasingPathV2(matrix))
