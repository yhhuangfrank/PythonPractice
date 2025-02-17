from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        arr = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            maxCoins = 0
            for i in range(l, r + 1):
                coins = arr[i] * arr[l - 1] * arr[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                maxCoins = max(maxCoins, coins)
            dp[(l, r)] = maxCoins
            return dp[(l, r)]

        return dfs(1, len(arr) - 2)

sol = Solution()
print(sol.maxCoins([3, 1, 5, 8]))