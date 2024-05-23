# Given a string s and a dictionary of strings wordDict,
# return true if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
#
# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
#
# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
#
# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
from typing import List


class Solution:
    # brute force
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        def dfs(i):
            if i == len(s):
                return True
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in words and dfs(j):
                    return True
            return False

        return dfs(0)

    # memoization - top down
    def wordBreakV2(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        cache = set()

        def dfs(i):
            if i == len(s):
                return True
            if i in cache:
                return False

            for j in range(i + 1, len(s) + 1):
                if s[i:j] in words and dfs(j):
                    return True
            cache.add(i)
            return False

        return dfs(0)

    # DP - bottom up
    def wordBreakV3(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in words and dp[j]:
                    dp[i] = True
                    break
        return dp[0]


sol = Solution()
# print(sol.wordBreak("leetcode", ["leet", "code"]))
# print(sol.wordBreak("applepenapple", ["apple", "pen"]))
# print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
print("=-------------------------------------------------------------------------------")
# print(sol.wordBreakV2("leetcode", ["leet", "code"]))
# print(sol.wordBreakV2("applepenapple", ["apple", "pen"]))
# print(sol.wordBreakV2("catsandog", ["cats", "dog", "sand", "and", "cat"]))
# print(sol.wordBreakV2(
#     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
#     ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"])
# )
print("=-------------------------------------------------------------------------------")
print(sol.wordBreakV3("leetcode", ["leet", "code"]))
print(sol.wordBreakV3("applepenapple", ["apple", "pen"]))
print(sol.wordBreakV3("catsandog", ["cats", "dog", "sand", "and", "cat"]))
print(sol.wordBreakV3(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
    ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"])
)

