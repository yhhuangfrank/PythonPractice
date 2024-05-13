# For two strings s and t, we say "t divides s"
# if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
#
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
#
# Example 2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
#
# Example 3:
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        shorter = str1 if len(str1) <= len(str2) else str2

        def isCommonDivisor(string):
            if len(str1) % len(string) or len(str2) % len(string):
                return False
            f1, f2 = len(str1) // len(string), len(str2) // len(string)
            return str1 == string * f1 and str2 == string * f2

        for i in range(len(shorter) + 1, 0, -1):
            if isCommonDivisor(shorter[0:i]):
                return shorter[0:i]
        return ""


sol = Solution()
print(sol.gcdOfStrings("ABABAB", "ABAB"))
print(sol.gcdOfStrings("LEET", "CODE"))
