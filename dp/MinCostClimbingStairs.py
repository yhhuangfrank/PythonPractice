# You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
# Once you pay the cost, you can either climb one or two steps.
#
# You can either start from the step with index 0, or the step with index 1.
#
# Return the minimum cost to reach the top of the floor.
#
# Example 1:
# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
#
# Example 2:
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
from typing import List


class Solution:
    # brute force
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def dfs(i, prev):
            if i >= len(cost):
                return prev
            return prev + min(
                dfs(i + 1, cost[i]),
                dfs(i + 2, cost[i])
            )

        return min(dfs(0, 0), dfs(1, 0))

    # memoization top-down, O(n) time, O(n) space
    def minCostClimbingStairsV2(self, cost: List[int]) -> int:
        cache = {}

        def dfs(i, prev):
            if i >= len(cost):
                return prev
            if i in cache:
                return prev + cache[i]
            cache[i] = min(
                dfs(i + 1, cost[i]),
                dfs(i + 2, cost[i])
            )
            return prev + cache[i]

        return min(dfs(0, 0), dfs(1, 0))

    # DP solution - bottom up, O(n) time, O(1) space
    def minCostClimbingStairsV3(self, cost: List[int]) -> int:
        dp = [0, 0]
        for i in range(len(cost) - 1, -1, -1):
            temp = cost[i] + min(dp[0], dp[1])
            dp[1] = dp[0]
            dp[0] = temp
        return min(dp)


sol = Solution()
arr1 = [10, 15, 20]
arr2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(sol.minCostClimbingStairs(arr1))
print(sol.minCostClimbingStairs(arr2))
print(sol.minCostClimbingStairsV2(arr1))
print(sol.minCostClimbingStairsV2(arr2))
print(sol.minCostClimbingStairsV3(arr1))
print(sol.minCostClimbingStairsV3(arr2))
