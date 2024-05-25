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

class Solution:
    # DP O(n ^ 2) time, O(n ^ 2) space
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
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
    def longestCommonSubsequenceV2(self, text1: str, text2: str) -> int:
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
# print(sol.longestCommonSubsequence("abcde", "ace"))
print(sol.longestCommonSubsequenceV2("abcde", "ace"))
print(sol.longestCommonSubsequenceV2("abc", "abc"))
print(sol.longestCommonSubsequenceV2("abc", "def"))
