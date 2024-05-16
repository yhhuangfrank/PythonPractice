# 給定一 array ，每個數字代表 可跳躍的最大步數
# 問：從 index 0 出發，是否可以走到 last index

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what.
# Its maximum jump length is 0, which makes it impossible to reach the last index.
from typing import List


class Solution:
    # brute force
    def canJump(self, nums: List[int]) -> bool:

        def dfs(i):
            if i == len(nums) - 1:
                return True
            if nums[i] == 0:
                return False
            for j in range(1, nums[i] + 1):
                if dfs(i + j):
                    return True
            return False

        return dfs(0)

    # memoization
    def canJumpV2(self, nums: List[int]) -> bool:
        cache = set()

        def dfs(i):
            if i == len(nums) - 1:
                return True
            if nums[i] == 0:
                return False
            for j in range(1, nums[i] + 1):
                next_position = i + j
                if next_position in cache:
                    continue
                if dfs(next_position):
                    return True
            cache.add(i)  # 代表此 index 已經判斷過
            return False

        return dfs(0)

    # greedy
    def canJumpV3(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:  # 若能走到終點代表可將終點往前移動
                goal = i
        return goal == 0


sol = Solution()
arr = [3, 2, 1, 0, 4]
arr2 = [2, 5, 0, 0]
print(sol.canJump(arr))
print(sol.canJump(arr2))
print(sol.canJumpV2(arr))
print(sol.canJumpV2(arr2))
print(sol.canJumpV3(arr))
print(sol.canJumpV3(arr2))
