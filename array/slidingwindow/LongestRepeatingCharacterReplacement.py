# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
#
# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.

class Solution:
    # O(26N) -> O(N) time
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        count = {}
        l, r = 0, 0
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            curLen = r - l + 1
            if curLen - max(count.values()) > k:
                count[s[l]] = count.get(s[l], 0) - 1
                l += 1
                curLen -= 1
            maxLength = max(maxLength, curLen)
            r += 1
        return maxLength

    # O(N) time
    def characterReplacementV1(self, s: str, k: int) -> int:
        maxLength = 0
        count = {}
        l, r = 0, 0
        maxf = 0  # 紀錄最多出現個數
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])
            curLen = r - l + 1
            if curLen - maxf > k:
                count[s[l]] -= 1
                l += 1
                curLen -= 1
            maxLength = max(maxLength, curLen)
            r += 1
        return maxLength


sol = Solution()
print(sol.characterReplacement("ABAB", 2))
print(sol.characterReplacement("AABABBA", 1))
print(sol.characterReplacementV1("ABAB", 2))
print(sol.characterReplacementV1("AABABBA", 1))
