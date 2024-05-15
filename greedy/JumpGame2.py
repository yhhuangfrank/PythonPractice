# Jump Game 的延伸，改問到 last index 所花費最少步數為何？
from typing import List


class Solution:
    # brute force
    def jump(self, nums: List[int]) -> int:
        minStep = [float('inf')]

        def dfs(i, currSteps):
            if i >= len(nums) - 1:
                minStep[0] = min(minStep[0], currSteps)
                return
            if nums[i] == 0:
                return
            for step in range(1, nums[i] + 1):
                dfs(i + step, currSteps + 1)

        dfs(0, 0)
        return int(minStep[0])

    # 類似 BFS
    def jumpV2(self, nums: List[int]) -> int:
        l, r = 0, 0  # window
        step = 0
        while r < len(nums) - 1:
            # 決定最遠位置
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l, r = r + 1, farthest
            step += 1
        return step


sol = Solution()
arr = [2, 5, 0, 0]
arr2 = [2, 3, 1, 1, 4]
arr3 = [1, 2, 1, 1, 1]
print(sol.jumpV2(arr))
print(sol.jumpV2(arr2))
print(sol.jumpV2(arr3))
