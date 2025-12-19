from collections import defaultdict
from typing import List

# Input: m = 3, n = 3, coordinates = [[0,0]]
# Output: [3,1,0,0,0]
# Input: m = 3, n = 3, coordinates = [[0,0],[1,1],[0,2]]
# Output: [0,2,2,0,0]
class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        blockToCount = defaultdict(int)
        ROWS, COLS = m, n
        # 從黑色格子統計每個至少含有一塊黑色格子的區塊
        # 每個格子視為區塊的左上角
        for r, c in coordinates:
            # 區塊1: 左上角為 (r - 1, c - 1)
            if 0 <= r - 1 < ROWS - 1 and 0 <= c - 1 < COLS - 1:
                blockToCount[(r - 1, c - 1)] += 1
            # 區塊2: 左上角為 (r - 1, c)
            if 0 <= r - 1 < ROWS - 1 and 0 <= c < COLS - 1:
                blockToCount[(r - 1, c)] += 1
            # 區塊3: 左上角為 (r, c - 1)
            if 0 <= r < ROWS - 1 and 0 <= c - 1 < COLS - 1:
                blockToCount[(r, c - 1)] += 1
            # 區塊4: 左上角為 (r, c)
            if 0 <= r < ROWS - 1 and 0 <= c < COLS - 1:
                blockToCount[(r, c)] += 1

        res = [0] * 5
        # 統計不同黑格子數的區塊數量
        for cnt in blockToCount.values():
            res[cnt] += 1
        # 統計沒有黑格子的區塊數，總共可組成的區塊數為 (m - 1) * (n - 1)
        res[0] = (m - 1) * (n - 1) - len(blockToCount)
        return res

sol = Solution()
print(sol.countBlackBlocks(m=3, n=3, coordinates=[[0, 0]]))
print(sol.countBlackBlocks(m=3, n=3, coordinates=[[0, 0], [1, 1], [0, 2]]))
