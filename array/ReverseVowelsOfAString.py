# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and
# they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "hello"
# Output: "holle"
#
# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelSet = {"a", "e",  "i", "o", "u", "A", "E", "I", "O", "U"}
        vowels = []

        for i in range(len(s)):
            c = s[i]
            if c in vowelSet:
                vowels.append((c, i))

        sList = list(s)
        for i in range(len(vowels) - 1, -1, -1):
            nc = vowels[i][0]
            idx = vowels[len(vowels) - 1 - i][1]  # 原先的 idx 位置
            sList[idx] = nc
        return "".join(sList)


sol = Solution()
print(sol.reverseVowels("leetcode"))
print(sol.reverseVowels("aA"))
