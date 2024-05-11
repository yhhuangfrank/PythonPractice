# You are given a 𝑚 × 𝑛 2D grid initialized with these three possible values:
#
# -1 - A water cell that can not be traversed.
# 0 - A treasure chest.
# INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
#
# Fill each land cell with the distance to its nearest treasure chest.
# If a land cell cannot reach a treasure chest than the value should remain INF.
# Assume the grid can only be traversed up, down, left, or right.

# Input: [
#   [2147483647,-1,0,2147483647],
#   [2147483647,2147483647,2147483647,-1],
#   [2147483647,-1,2147483647,-1],
#   [0,-1,2147483647,2147483647]
# ]
#
# Output: [
#   [3,-1,0,1],
#   [2,2,1,-1],
#   [1,-1,2,-1],
#   [0,-1,3,4]
# ]
from typing import List
from collections import deque


class Solution:
    # O((m * n) ^ 2) time，從 land 出發
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            dist = 0
            visited = set()
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            while queue:
                size = len(queue)
                for _ in range(size):
                    r, c = queue.popleft()
                    if grid[r][c] == 0:
                        return dist
                    visited.add((r, c))
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (
                                min(nr, nc) < 0 or nr == ROWS or nc == COLS
                                or grid[nr][nc] == -1 or (nr, nc) in visited
                        ):
                            continue
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                dist += 1
            return dist

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == INF:
                    distance = bfs(row, col)
                    grid[row][col] = INF if distance == 0 else distance

    # O(m * n) time, 從 treasure 角度出發
    def islandsAndTreasureV2(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        queue = deque()

        # 加入所有的 treasure 到 queue，讓 bfs 是從所有 treasure 開始同步向前
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col))
                    visited[row][col] = True

        # bfs
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        distance = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                visited[r][c] = True
                grid[r][c] = distance
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                            min(nr, nc) < 0 or nr == ROWS or nc == COLS
                            or grid[nr][nc] == -1 or visited[nr][nc]
                    ):
                        continue
                    queue.append((nr, nc))
                    visited[nr][nc] = True
            distance += 1


sol = Solution()
grid = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647]
]
grid2 = grid.copy()
sol.islandsAndTreasure(grid)
sol.islandsAndTreasureV2(grid2)
print(grid)
print(grid2)
