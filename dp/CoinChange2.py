# Coin Change 的續題，改問共有幾種組合，若找不到組合，回傳 0
#
# Example 1:
# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#
# Example 2:
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
#
# Example 3:
# Input: amount = 10, coins = [10]
# Output: 1
import time
from typing import List


class Solution:
    # brute force, O(len(coins) ^ amount)
    def change(self, amount: int, coins: List[int]) -> int:

        def dfs(i, remain):
            if i == len(coins):
                return 1 if remain == 0 else 0
            # skip
            count = dfs(i + 1, remain)
            # include
            newRemain = remain - coins[i]
            if newRemain >= 0:
                count += dfs(i, newRemain)
            return count

        return dfs(0, amount)

    # memoization, O(len(coins) * amount) time
    def changeV2(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dfs(i, remain):
            if i == len(coins):
                return 1 if remain == 0 else 0
            if (i, remain) in cache:
                return cache[(i, remain)]
            # skip
            cache[(i, remain)] = dfs(i + 1, remain)
            # include
            newRemain = remain - coins[i]
            if newRemain >= 0:
                cache[(i, remain)] += dfs(i, newRemain)
            return cache[(i, remain)]

        return dfs(0, amount)

    # DP, O(len(coins) * amount) time, O(len(coins) * amount) space
    def changeV3(self, amount: int, coins: List[int]) -> int:
        coinNum, amounts = len(coins) + 1, amount + 1
        dp = [[0] * amounts for _ in range(coinNum)]
        for r in range(coinNum):
            dp[r][0] = 1

        for c in range(1, coinNum):
            for a in range(1, amounts):
                dp[c][a] = dp[c - 1][a]  # skip
                remain = a - coins[c - 1]
                if remain >= 0:
                    dp[c][a] += dp[c][remain]  # include
        return dp[-1][-1]

    # optimized DP, O(len(coins) * amount) time, O(amount) space
    def changeV4(self, amount: int, coins: List[int]) -> int:
        coinNum, amounts = len(coins) + 1, amount + 1
        dp = [0] * amounts

        for c in range(1, coinNum):
            new_dp = [0] * amounts
            new_dp[0] = 1
            for a in range(1, amounts):
                new_dp[a] = dp[a]  # skip
                remain = a - coins[c - 1]  # coinNum 多一列，需減 1 來對應 coins list
                if remain >= 0:
                    new_dp[a] += new_dp[remain]  # include
            dp = new_dp
        return dp[-1]


sol = Solution()
arr1 = [1, 2, 5]
arr2 = [2]
arr3 = [3, 5, 7, 8, 9, 10, 11]
t1 = time.time()
print("brute force")
print(sol.change(5, arr1))
print(sol.change(3, arr2))
print(sol.change(100, arr3))
t2 = time.time()
diff1 = t2 - t1
print(diff1)
print("==============================")
print("memoization")
t1 = time.time()
print(sol.changeV2(5, arr1))
print(sol.changeV2(3, arr2))
print(sol.changeV2(100, arr3))
t2 = time.time()
diff2 = t2 - t1
print(diff2)
print(diff1 / diff2)
print("==============================")
print("dp")
t1 = time.time()
print(sol.changeV3(5, arr1))
print(sol.changeV3(3, arr2))
print(sol.changeV3(100, arr3))
t2 = time.time()
diff2 = t2 - t1
print(diff2)
print(diff1 / diff2)
print("==============================")
print("optimized dp")
t1 = time.time()
print(sol.changeV4(5, arr1))
print(sol.changeV4(3, arr2))
print(sol.changeV4(100, arr3))
t2 = time.time()
diff2 = t2 - t1
print(diff2)
print(diff1 / diff2)
