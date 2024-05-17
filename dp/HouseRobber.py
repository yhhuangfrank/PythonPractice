# 一 array 代表一排房子內的錢，小偷若偷了某一間必須間隔一間才能再偷，否則會觸發警報
# 問小偷能獲得的最大收益為何？
# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
#
# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
from typing import List


class Solution:
    # memoization (top down)
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dfs(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return cache[i]

        return dfs(0)

    # bottom up DP
    def robV2(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


sol = Solution()
print(sol.rob([1, 2, 3, 1]))
print(sol.robV2([1, 2, 3, 1]))
print(sol.rob([2, 7, 9, 3, 1]))
print(sol.robV2([2, 7, 9, 3, 1]))
