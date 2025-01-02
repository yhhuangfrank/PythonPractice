# Example 1:
# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# 
# Example 2:
# Input: s = "babgbag", t = "bag"
# Output: 5

class Solution:
    # m = len(s) + len(t)
    # O(2^m) time
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            res = dfs(i + 1, j) # skip
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            return res
        
        return dfs(0, 0)
    
    # O(len(s) * len(t)) time
    def numDistinctV2(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        cache = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            cache[(i, j)] = dfs(i + 1, j) # skip
            if s[i] == t[j]:
                cache[(i, j)] += dfs(i + 1, j + 1)
            return cache[(i, j)]
        
        return dfs(0, 0)
    
    # O(len(s) * len(t)) time
    def numDistinctV3(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        ROWS, COLS = len(s) + 1, len(t) + 1
        dp = [[0] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            dp[r][-1] = 1
        
        for r in range(len(s) - 1, -1, -1):
            for c in range(len(t) - 1, -1, -1):
                dp[r][c] = dp[r + 1][c]
                if s[r] == t[c]:
                    dp[r][c] += dp[r + 1][c + 1]
        return dp[0][0]
    
    # O(len(s) * len(t)) time
    def numDistinctV4(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        dp = [0] * (len(t) + 1)
        dp[-1] = 1

        for r in range(len(s) - 1, -1, -1):
            new_dp = [0] * (len(t) + 1)
            new_dp[-1] = 1
            for c in range(len(t) - 1, -1, -1):
                new_dp[c] = dp[c]
                if s[r] == t[c]:
                    new_dp[c] += dp[c + 1]
            dp = new_dp
        return dp[0]


sol = Solution()
# print(sol.numDistinct("rabbbit", "rabbit")) # 3
# print(sol.numDistinct("babgbag", "bag")) # 5
# print(sol.numDistinct("daacaedaceacabbaabdccdaaeaebacddadcaeaacadbceaecddecdeedcebcdacdaebccdeebcbdeaccabcecbeeaadbccbaeccbbdaeadecabbbedceaddcdeabbcdaeadcddedddcececbeeabcbecaeadddeddccbdbcdcbceabcacddbbcedebbcaccac", "ceadbaa")) # 8556153
# print(sol.numDistinctV2("daacaedaceacabbaabdccdaaeaebacddadcaeaacadbceaecddecdeedcebcdacdaebccdeebcbdeaccabcecbeeaadbccbaeccbbdaeadecabbbedceaddcdeabbcdaeadcddedddcececbeeabcbecaeadddeddccbdbcdcbceabcacddbbcedebbcaccac", "ceadbaa")) # 8556153
print(sol.numDistinctV3("babgbag", "bag")) # 5
print(sol.numDistinctV4("babgbag", "bag")) # 5
print(sol.numDistinctV4("daacaedaceacabbaabdccdaaeaebacddadcaeaacadbceaecddecdeedcebcdacdaebccdeebcbdeaccabcecbeeaadbccbaeccbbdaeadecabbbedceaddcdeabbcdaeadcddedddcececbeeabcbecaeadddeddccbdbcdcbceabcacddbbcedebbcaccac", "ceadbaa")) # 8556153
