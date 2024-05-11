from collections import deque
from typing import List


class Solution:
    # 使用 bfs
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False] * COLS for _ in range(ROWS)]

        def bfs(i, j):
            area = 0
            queue = deque()
            queue.append((i, j))
            deviations = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            while queue:
                size = len(queue)
                area += size
                for _ in range(size):
                    r, c = queue.popleft()
                    visited[r][c] = True
                    for dr, dc in deviations:
                        nr, nc = r + dr, c + dc
                        if (min(nr, nc) < 0 or nr == ROWS or nc == COLS
                                or grid[nr][nc] != 1 or visited[nr][nc]):
                            continue
                        queue.append((nr, nc))
                        visited[nr][nc] = True
            return area

        maxArea = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and not visited[row][col]:
                    maxArea = max(maxArea, bfs(row, col))
        return maxArea

    # 使用 dfs
    def maxAreaOfIslandV2(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False] * COLS for _ in range(ROWS)]

        def dfs(r, c):
            if (
                    min(r, c) < 0 or r == ROWS or c == COLS
                    or grid[r][c] == 0 or visited[r][c]
            ):
                return 0

            visited[r][c] = True
            area = 1
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area

        maxArea = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and not visited[row][col]:
                    maxArea = max(maxArea, dfs(row, col))
        return maxArea


sol = Solution()
grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
]
print(sol.maxAreaOfIsland(grid))  # 6
print(sol.maxAreaOfIslandV2(grid))  # 6
