# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
#
# An interleaving of two strings s and t is a configuration where s and t are divided into n and m
# substrings respectively
# Example 1:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Explanation: One way to obtain s3 is:
# Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
# Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
# Since s3 can be obtained by interleaving s1 and s2, we return true.
#
# Example 2:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
#
# Example 3:
# Input: s1 = "", s2 = "", s3 = ""
# Output: true

class Solution:
    # brute force
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True

            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True
            return False

        return dfs(0, 0)

    # memoization
    def isInterleaveV2(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        cache = {}

        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in cache:
                return cache[(i, j)]

            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                cache[(i, j)] = True
            elif j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                cache[(i, j)] = True
            else:
                cache[(i, j)] = False
            return cache[(i, j)]

        return dfs(0, 0)

    # DP, O(len(s1) * len(s2)) time, O(len(s1) * len(s2)) space
    def isInterleaveV3(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        ROWS, COLS = len(s1) + 1, len(s2) + 1
        dp = [[False] * COLS for _ in range(ROWS)]
        dp[-1][-1] = True

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if r < len(s1) and s1[r] == s3[r + c] and dp[r + 1][c]:
                    dp[r][c] = True
                if c < len(s2) and s2[c] == s3[r + c] and dp[r][c + 1]:
                    dp[r][c] = True
        return dp[0][0]

    # optimized DP, O(len(s1) * len(s2)) time, O(len(s2)) space
    def isInterleaveV4(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        ROWS, COLS = len(s1) + 1, len(s2) + 1
        dp = [False] * COLS
        dp[-1] = True
        for c in range(COLS - 2, -1, -1):
            if c < len(s2) and s2[c] == s3[ROWS - 1 + c] and dp[c + 1]:
                dp[c] = True

        for r in range(ROWS - 2, -1, -1):
            new_dp = [False] * COLS
            for c in range(COLS - 1, -1, -1):
                if r < len(s1) and s1[r] == s3[r + c] and dp[c]:
                    new_dp[c] = True
                if c < len(s2) and s2[c] == s3[r + c] and new_dp[c + 1]:
                    new_dp[c] = True
            dp = new_dp
        return dp[0]


sol = Solution()
# print(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
# print(sol.isInterleave("aabcc", "dbbca", "aadbbcbccc"))
# print(sol.isInterleave("", "", ""))
#
# print("=====================")
#
# print(sol.isInterleaveV2("aabcc", "dbbca", "aadbbcbcac"))
# print(sol.isInterleaveV2("aabcc", "dbbca", "aadbbcbccc"))
# print(sol.isInterleaveV2("", "", ""))
#
# print("=====================")

print(sol.isInterleaveV3("aabcc", "dbbca", "aadbbcbcac"))  # True
print(sol.isInterleaveV3("aabcc", "dbbca", "aadbbcbccc"))  # False
print(sol.isInterleaveV3("bbbcc", "bbaccbbbabcacc", "bbbbacbcccbcbabbacc"))  # False

print("=====================")

print(sol.isInterleaveV4("aabcc", "dbbca", "aadbbcbcac"))
print(sol.isInterleaveV4("aabcc", "dbbca", "aadbbcbccc"))
print(sol.isInterleaveV4("bbbcc", "bbaccbbbabcacc", "bbbbacbcccbcbabbacc"))
