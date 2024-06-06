# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
#
# You have the following three operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character
#
# Example 1:
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#
# Example 2:
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
import time


class Solution:
    # brute force, O(3 ^ (m + n)) time, O(n * m) space
    def minDistance(self, word1: str, word2: str) -> int:

        def dfs(i, j):
            # 滿足 i == len(word1) or j == len(word2)，剩餘需要的步驟數量就是剩下的字母數
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            else:
                return 1 + min(
                    dfs(i, j + 1),  # insert
                    dfs(i + 1, j + 1),  # replace
                    dfs(i + 1, j)  # delete
                )

        return dfs(0, 0)

    # memoization, O(m * n) time, O(m * n) space
    def minDistanceV2(self, word1: str, word2: str) -> int:
        cache = {}

        def dfs(i, j):
            # 滿足 i == len(word1) or j == len(word2)，剩餘需要的步驟數量就是剩下的字母數
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i, j) in cache:
                return cache[(i, j)]
            if word1[i] == word2[j]:
                cache[(i, j)] = dfs(i + 1, j + 1)
            else:
                cache[(i, j)] = 1 + min(
                    dfs(i, j + 1),  # insert
                    dfs(i + 1, j + 1),  # replace
                    dfs(i + 1, j)  # delete
                )
            return cache[(i, j)]

        return dfs(0, 0)

    # DP, O(m * n) time, O(m * n) space
    def minDistanceV3(self, word1: str, word2: str) -> int:
        ROWS, COLS = len(word1) + 1, len(word2) + 1
        dp = [[0] * COLS for _ in range(ROWS)]

        # base case
        for r in range(ROWS - 1, -1, -1):
            dp[r][-1] = ROWS - 1 - r
        for c in range(COLS - 1, -1, -1):
            dp[-1][c] = COLS - 1 - c

        for r in range(ROWS - 2, -1, -1):
            for c in range(COLS - 2, -1, -1):
                if word1[r] == word2[c]:
                    dp[r][c] = dp[r + 1][c + 1]
                else:
                    dp[r][c] = 1 + min(
                        dp[r][c + 1],
                        dp[r + 1][c + 1],
                        dp[r + 1][c]
                    )
        return dp[0][0]


sol = Solution()
print("brute force")
t1 = time.time()
print(sol.minDistance("horse", "ros"))
print(sol.minDistance("intention", "execution"))
t2 = time.time()
diff1 = t2 - t1
print(diff1)

print("===================")
print("memoization")
t1 = time.time()
print(sol.minDistanceV2("horse", "ros"))
print(sol.minDistanceV2("intention", "execution"))
t2 = time.time()
diff2 = t2 - t1
print(diff2)
print(diff1 / diff2)

print("===================")
print("DP")
t1 = time.time()
print(sol.minDistanceV3("horse", "ros"))
print(sol.minDistanceV3("intention", "execution"))
t2 = time.time()
diff2 = t2 - t1
print(diff2)

print(diff1 / diff2)

