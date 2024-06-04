# Example 1:
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.
#
# Example 2:
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
#
# Example 3:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
import time


class Solution:

    # brute force, O(2^(m+n)) time, O(m + n) space
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def dfs(i1, i2):
            if i1 == len(text1) or i2 == len(text2):
                return 0
            # 兩字母相同，往下找子問題
            if text1[i1] == text2[i2]:
                return 1 + dfs(i1 + 1, i2 + 1)
            return max(dfs(i1 + 1, i2), dfs(i1, i2 + 1))

        return dfs(0, 0)

    # memoization, O(m * n) time, O(m * n) space
    def longestCommonSubsequenceV2(self, text1: str, text2: str) -> int:
        cache = {}

        def dfs(i1, i2):
            if i1 == len(text1) or i2 == len(text2):
                return 0
            if (i1, i2) in cache:
                return cache[(i1, i2)]
            # 兩字母相同，往下找子問題
            if text1[i1] == text2[i2]:
                cache[(i1, i2)] = 1 + dfs(i1 + 1, i2 + 1)
            else:
                cache[(i1, i2)] = max(dfs(i1 + 1, i2), dfs(i1, i2 + 1))
            return cache[(i1, i2)]

        return dfs(0, 0)

    # DP O(n ^ 2) time, O(n ^ 2) space
    def longestCommonSubsequenceV3(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        ROWS, COLS = len(dp), len(dp[0])
        for r in range(1, ROWS):
            for c in range(1, COLS):
                c1, c2 = text1[c - 1], text2[r - 1]
                if c1 == c2:
                    dp[r][c] = dp[r - 1][c - 1] + 1
                else:
                    dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])
        return dp[ROWS - 1][COLS - 1]

    # O(n ^ 2) time, O(n) space
    def longestCommonSubsequenceV4(self, text1: str, text2: str) -> int:
        ROWS, COLS = len(text2) + 1, len(text1) + 1
        dp = [0] * COLS
        for r in range(1, ROWS):
            new_dp = [0] * COLS
            for c in range(1, COLS):
                c1, c2 = text1[c - 1], text2[r - 1]
                if c1 == c2:
                    new_dp[c] = dp[c - 1] + 1
                else:
                    new_dp[c] = max(dp[c], new_dp[c - 1])
            dp = new_dp
        return dp[-1]


sol = Solution()
t1 = time.time()
print("brute force")
print(sol.longestCommonSubsequence("abcdegegegeg", "acegeaetmkizign"))  # 3
print(sol.longestCommonSubsequence("abc", "abc"))  # 3
print(sol.longestCommonSubsequence("abc", "def"))  # 0
t2 = time.time()
diff1 = t2 - t1
print(diff1)

print("===========================================================")
print("memoization")
t1 = time.time()
print(sol.longestCommonSubsequenceV2("abcdegegegeg", "acegeaetmkizign"))
print(sol.longestCommonSubsequenceV2("abc", "abc"))
print(sol.longestCommonSubsequenceV2("abc", "def"))
t2 = time.time()
diff2 = t2 - t1
print(diff2)
print(diff1 / diff2)

print("===========================================================")
print("DP")
t1 = time.time()
print(sol.longestCommonSubsequenceV3("abcdegegegeg", "acegeaetmkizign"))
print(sol.longestCommonSubsequenceV3("abc", "abc"))
print(sol.longestCommonSubsequenceV3("abc", "def"))
t2 = time.time()
diff2 = t2 - t1
print(diff2)
print(diff1 / diff2)

print("===========================================================")
print("optimized DP")
t1 = time.time()
print(sol.longestCommonSubsequenceV4("abcdegegegeg", "acegeaetmkizign"))
print(sol.longestCommonSubsequenceV4("abc", "abc"))
print(sol.longestCommonSubsequenceV4("abc", "def"))
t2 = time.time()
diff2 = t2 - t1
print(diff2)
print(diff1 / diff2)
