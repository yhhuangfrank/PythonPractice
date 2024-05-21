# Given a string s, return the longest palindromic substring in s.
#
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
# Example 2:
# Input: s = "cbbd"
# Output: "bb"

class Solution:
    # brute force, O(n^3) time
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        res = ""

        def isPalindrome(string):
            start, end = 0, len(string) - 1
            while start < end:
                if string[start] != string[end]:
                    return False
                start += 1
                end -= 1
            return True

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]
                if isPalindrome(sub) and len(sub) > maxLen:
                    maxLen = len(sub)
                    res = sub
        return res

    # O(n^2) time
    def longestPalindromeV2(self, s: str) -> str:
        if len(s) == 1:
            return s
        maxLen = 0
        res = ""

        for i in range(len(s)):
            # 奇數長度
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    res = s[l:r + 1]
                l -= 1
                r += 1
            # 偶數長度
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    res = s[l:r + 1]
                l -= 1
                r += 1
        return res


sol = Solution()
# print(sol.longestPalindrome("babad"))
# print(sol.longestPalindrome("cbbd"))
print(sol.longestPalindromeV2("babad"))
print(sol.longestPalindromeV2("babab"))
print(sol.longestPalindromeV2("cbbd"))
