# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
#
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isAlphanumeric(c):
            return ord("a") <= ord(c) <= ord("z") or ord("0") <= ord(c) <= ord("9")

        newS = s.strip()
        l, r = 0, len(newS) - 1

        while l < r:
            lchar, rchar = newS[l].lower(), newS[r].lower()
            if not isAlphanumeric(lchar):
                l += 1
            elif not isAlphanumeric(rchar):
                r -= 1
            elif lchar != rchar:
                return False
            else:
                l += 1
                r -= 1
        return True


sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome("race a car"))
print(sol.isPalindrome(" "))
