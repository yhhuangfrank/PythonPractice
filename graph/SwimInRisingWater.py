# You are given an n x n integer matrix grid where each value grid[i][j] 
# represents the elevation at that point (i, j).
#
# The rain starts to fall. At time t, the depth of the water everywhere is t.
# You can swim from a square to another 4-directionally adjacent square 
# if and only if the elevation of both squares individually are at most t. 
# You can swim infinite distances in zero time. 
# Of course, you must stay within the boundaries of the grid during your swim.
#
# Return the least time until you can reach the bottom right square (n - 1, n - 1) 
# if you start at the top left square (0, 0).
#
# 
# Input: grid = [[0,2],[1,3]]
# Output: 3
# Explanation:
# At time 0, you are in grid location (0, 0).
# You cannot go anywhere else because 4-directionally adjacent neighbors 
# have a higher elevation than t = 0.
# You cannot reach point (1, 1) until time 3.
# When the depth of water is 3, we can swim anywhere inside the grid.

import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        minHeap = [(grid[0][0],0,0)]
        visit.add((0,0))

        while minHeap:
            h, x, y = heapq.heappop(minHeap)
            if x == ROWS - 1 and y == COLS - 1:
                return h
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if (
                    min(nx, ny) < 0 or nx == ROWS or ny == COLS
                    or (nx, ny) in visit
                ):
                    continue
                visit.add((nx, ny))
                heapq.heappush(minHeap, (max(grid[nx][ny], h), nx, ny)) 

sol = Solution()
grid1 = [[0, 2], [1, 3]]
grid2 = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
print(sol.swimInWater(grid1)) # 3
print(sol.swimInWater(grid2)) # 16