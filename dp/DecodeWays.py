# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F'
# since "6" is different from "06".
# Given a string s containing only digits, return the number of ways to decode it.
# The test cases are generated so that the answer fits in a 32-bit integer.
#
# Example 1:
# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
#
# Example 2:
# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
#
# Example 3:
# Input: s = "06"
# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

class Solution:
    # brute force, O(2^n)
    def numDecodings(self, s: str) -> int:

        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            res = dfs(i + 1)
            if i + 1 < len(s) and 10 <= int(s[i: i + 2]) <= 26:
                res += dfs(i + 2)
            return res

        return dfs(0)

    # memoization, O(n) time
    def numDecodingsV2(self, s: str) -> int:
        cache = {len(s): 1}

        def dfs(i):
            if i in cache:
                return cache[i]
            if s[i] == "0":
                return 0
            res = dfs(i + 1)
            if i + 1 < len(s) and 10 <= int(s[i:i + 2]) <= 26:
                res += dfs(i + 2)
            cache[i] = res
            return cache[i]

        dfs(0)
        return cache.get(0, 0)

    # DP solution
    def numDecodingsV3(self, s: str) -> int:
        # dp[i] = dp[i + 1] + dp[i + 2]
        dp = [1, 0]
        for i in range(len(s) - 1, -1, -1):
            temp = 0
            if s[i] != "0":
                temp += dp[0]
                if i + 1 < len(s) and 10 <= int(s[i:i + 2]) <= 26:
                    temp += dp[1]
            dp[1] = dp[0]
            dp[0] = temp
        return dp[0]


sol = Solution()
# print(sol.numDecodings("226"))
# print(sol.numDecodings("06"))
# print(sol.numDecodings("11106"))
# print(sol.numDecodingsV2("226"))
# print(sol.numDecodingsV2("06"))
# print(sol.numDecodingsV2("11106"))
# print(sol.numDecodingsV3("226"))
print(sol.numDecodingsV3("06"))
print(sol.numDecodingsV3("11106"))
