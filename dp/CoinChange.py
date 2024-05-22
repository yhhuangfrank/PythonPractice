# You are given an integer array coins representing coins of different denominations
# and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.
#
# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
# Example 2:
# Input: coins = [2], amount = 3
# Output: -1
#
# Example 3:
# Input: coins = [1], amount = 0
# Output: 0
from typing import List


class Solution:
    # brute force
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        def dfs(i, remain):
            if remain == 0:
                return 0
            if i == len(coins):
                return -1

            ans = float("inf")
            for j in range((amount // coins[i]) + 1):
                t = dfs(i + 1, remain - coins[i] * j)
                if t >= 0:
                    ans = min(ans, t + j)
            return ans

        res = dfs(0, amount)
        return res if res != float("inf") else -1

    # memoization, top-down
    def coinChangeV2(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        cache = {}
        INF = float("inf")

        def dfs(remain):
            if remain in cache:
                return cache[remain]
            if remain < 0:
                return INF
            if remain == 0:
                return 0
            ans = INF
            for num in coins:
                t = dfs(remain - num)
                if t != INF:
                    ans = min(ans, 1 + t)
            cache[remain] = ans
            return cache[remain]

        res = dfs(amount)
        return res if res != INF else -1


sol = Solution()
arr1 = [1, 2, 5]
arr2 = [2]
arr3 = [1]
arr4 = [186, 419, 83, 408]
arr5 = [2]
# print(sol.coinChange(arr1, 11))
# print(sol.coinChange(arr2, 3))
# print(sol.coinChange(arr3, 0))
# print(sol.coinChange(arr4, 6249))
# print(sol.coinChange(arr5, 4))
print("==============================")
print(sol.coinChangeV2(arr1, 11))
print(sol.coinChangeV2(arr2, 3))
print(sol.coinChangeV2(arr3, 0))
print(sol.coinChangeV2(arr4, 6249))
print(sol.coinChangeV2(arr5, 4))
