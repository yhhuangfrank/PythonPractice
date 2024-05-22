# Given a string s, return the number of palindromic substrings in it.
#
# A string is a palindrome when it reads the same backward as forward.
#
# A substring is a contiguous sequence of characters within the string.
#
# Example 1:
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
# Example 2:
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

class Solution:
    # brute force, O(n^3) time
    def countSubstrings(self, s: str) -> int:
        count = 0

        def isPalindrome(string):
            l, r = 0, len(string) - 1
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if isPalindrome(s[i:j]):
                    count += 1
        return count

    # O(n^2) time
    def countSubstringsV2(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            l, r = i, i + 1
            # even length
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count


sol = Solution()
print(sol.countSubstrings("abc"))
print(sol.countSubstrings("aaa"))
print(sol.countSubstringsV2("abc"))
print(sol.countSubstringsV2("aaa"))
