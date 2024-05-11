# You are given an m x n grid where each cell can have one of three values:
#
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.
# If this is impossible, return -1.

# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0)
# is never rotten, because rotting only happens 4-directionally.

# Example 3:
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # bfs
        def bfs(freshCount):
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            time = 0
            while queue:
                time += 1
                size = len(queue)
                for _ in range(size):
                    r, c = queue.popleft()
                    visited[r][c] = True
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (
                                min(nr, nc) < 0 or nr == ROWS or nc == COLS
                                or grid[nr][nc] == 0 or visited[nr][nc]
                        ):
                            continue
                        queue.append((nr, nc))
                        freshCount[0] -= 1
                        visited[nr][nc] = True
                if not freshCount[0]:  # 沒有 fresh 橘子了
                    break
            return time

        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visited = [[False] * COLS for _ in range(ROWS)]
        freshCount = [0]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row, col))
                    visited[row][col] = True
                elif grid[row][col] == 1:
                    freshCount[0] += 1

        if freshCount[0] == 0:
            return 0
        time = bfs(freshCount)
        return -1 if freshCount[0] else time


sol = Solution()
grid1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
grid2 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
grid3 = [[0, 2]]
print(sol.orangesRotting(grid1))
print(sol.orangesRotting(grid2))
print(sol.orangesRotting(grid3))

