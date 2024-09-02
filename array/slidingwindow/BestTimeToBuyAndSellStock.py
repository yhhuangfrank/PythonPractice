# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
#
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
from typing import List


class Solution:
    # O(N^2) time
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        maxP = 0
        for s in range(len(prices) - 1):
            for e in range(s, len(prices)):
                maxP = max(maxP, prices[e] - prices[s])
        return maxP

    # O(N) time
    def maxProfitV1(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        maxP = 0
        s = 0  # 買入點
        for i in range(1, len(prices)):
            maxP = max(maxP, prices[i] - prices[s])
            s = i if prices[i] < prices[s] else s  # 更低的買入點
        return maxP


sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
print(sol.maxProfit([7, 6, 4, 3, 1]))
print(sol.maxProfitV1([7, 1, 5, 3, 6, 4]))
print(sol.maxProfitV1([7, 6, 4, 3, 1]))
