# 給定一 2D array 代表一座島嶼。島嶼上方與左方為太平洋、右方與下方為大西洋
# r, c 為 row, col。arr[r][c] 代表海平面高度
# 雨水可往 小於等於其高度的地方流。
# 問：可同時流向太平洋與大西洋的 (r,c) 組合

# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 105
# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

from typing import List
from collections import deque


class Solution:
    # O ((mn) ^ 2)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        def bfs(i, j):
            visited = set()
            queue = deque()
            queue.append((i, j))
            visited.add((i, j))
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            toAtlantic, toPacific = False, False
            while queue:
                size = len(queue)
                for _ in range(size):
                    r, c = queue.popleft()
                    h = heights[r][c]
                    if r == 0 or c == 0:
                        toPacific = True
                    if r == ROWS - 1 or c == COLS - 1:
                        toAtlantic = True
                    if toPacific and toAtlantic:
                        return True
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (
                                min(nr, nc) < 0 or nr == ROWS or nc == COLS
                                or heights[nr][nc] > h or (nr, nc) in visited
                        ):
                            continue
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            return False

        res = []
        for row in range(ROWS):
            for col in range(COLS):
                if bfs(row, col):
                    res.append([row, col])
        return res

    # O(mn) dfs
    # 想法：
    # 從第一 row, 第一 col 是一定可以流到 pac 的 cell，反向往中心點做 dfs，並標記可行的 cell
    # 同理對最後一 row, 最後一 col，反向往中心點做 dfs，並標記
    def pacificAtlanticV2(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, alt = set(), set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c, visited, prevHeight):
            if (
                    min(r, c) < 0 or r == ROWS or c == COLS
                    or heights[r][c] < prevHeight or (r, c) in visited
            ):
                return
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])  # first col
            dfs(r, COLS - 1, alt, heights[r][COLS - 1])  # last col
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])  # first row
            dfs(ROWS - 1, c, alt, heights[ROWS - 1][c])  # last row

        # 找到可流向兩邊的 row, col
        res = []
        for row in range(ROWS):
            for col in range(COLS):
                toPac, toAlt = (row, col) in pac, (row, col) in alt
                if toPac and toAlt:
                    res.append([row, col])
        return res


sol = Solution()
grid = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
]
print(sol.pacificAtlantic(grid))
print(sol.pacificAtlanticV2(grid))
