# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    # brute force, O(n^2) time, O(n) space)
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        for i in range(len(s)):
            charSet = set()  # check duplicates in O(1) time
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
                maxLen = max(maxLen, len(charSet))
        return maxLen

    #  sliding window, O(n) time, O(n) space
    def lengthOfLongestSubstringV2(self, s: str) -> int:
        charSet = set()
        maxLen = 0
        l, r = 0, 0
        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxLen = max(maxLen, len(charSet))
            r += 1
        return maxLen


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))
print(sol.lengthOfLongestSubstring("dvdf"))
print("=====================================")
print(sol.lengthOfLongestSubstringV2("abcabcbb"))
print(sol.lengthOfLongestSubstringV2("bbbbb"))
print(sol.lengthOfLongestSubstringV2("pwwkew"))
print(sol.lengthOfLongestSubstringV2("dvdf"))
