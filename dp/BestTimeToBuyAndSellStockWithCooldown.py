# 給定一 array prices，prices[i] 代表第 i 天的股票價格
# 每天可執行買賣，買賣規則為：
# 1. 必須買了才能賣
# 2. 賣了之後必須等待一天才能再買
# 問最大獲利為多少？
#
# Example 1:
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# Example 2:
# Input: prices = [1]
# Output: 0
from typing import List


class Solution:
    # brute force, O(2^n) time
    def maxProfit(self, prices: List[int]) -> int:

        def dfs(i, isSold):
            if i >= len(prices):
                return 0
            if isSold:
                return max(
                    dfs(i + 1, False) - prices[i],  # buy
                    dfs(i + 1, isSold)  # cooldown
                )
            return max(
                dfs(i + 1, isSold),  # cooldown
                dfs(i + 2, True) + prices[i]  # sell
            )

        return dfs(0, True)

    # memoization, O(n) time
    def maxProfitV2(self, prices: List[int]) -> int:
        cache = {}

        def dfs(i, isSold):
            if i >= len(prices):
                return 0
            if (i, isSold) in cache:
                return cache[(i, isSold)]
            if isSold:
                cache[(i, isSold)] = max(
                    dfs(i + 1, False) - prices[i],  # buy
                    dfs(i + 1, isSold)  # cooldown
                )
            else:
                cache[(i, isSold)] = max(
                    dfs(i + 1, isSold),  # cooldown
                    dfs(i + 2, True) + prices[i]  # sell
                )
            return cache[(i, isSold)]

        return dfs(0, True)
    
    # DP - bottom up
    def maxProfitV3(self, prices: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices))]
        ROWS, COLS = len(dp), len(dp[0])

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                cooldown = dp[r + 1][c] if r + 1 < ROWS else 0
                if c == 0: # previous one is buying
                    sell = prices[r] + dp[r + 2][1] if r + 2 < ROWS else prices[r]
                    dp[r][c] = max(sell, cooldown)
                else: # previous one is selling
                    buy = -prices[r] + dp[r + 1][0] if r + 1 < ROWS else -prices[r]
                    dp[r][c] = max(buy, cooldown)
        return dp[0][1]

sol = Solution()
arr1 = [1, 2, 3, 0, 2]
arr2 = [1]

# print(sol.maxProfit(arr1))
# print(sol.maxProfit(arr2))

print(sol.maxProfitV2(arr1))
print(sol.maxProfitV2(arr2))

print(sol.maxProfitV3(arr1))
print(sol.maxProfitV3(arr2))
