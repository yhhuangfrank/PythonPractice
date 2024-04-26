# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.


# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l, r = 0, 0
        letters = "abcdefghijklmnopqrstuvwxyz"
        s1Count = {}
        s2Count = {}
        for i in range(len(letters)):
            s1Count[letters[i]] = 0
            s2Count[letters[i]] = 0
        for i in range(len(s1)):
            s1Count[s1[i]] = s1Count[s1[i]] + 1
            s2Count[s2[i]] = s2Count[s2[i]] + 1
            r += 1

        matches = 0  # 需 26 個字母都對上
        for c in letters:
            matches += (1 if s1Count[c] == s2Count[c] else 0)
            if matches == 26:
                return True

        while r < len(s2):
            leftChar = s2[l]
            rightChar = s2[r]

            s2Count[leftChar] = s2Count[leftChar] - 1
            if s2Count[leftChar] == s1Count[leftChar] - 1:
                matches -= 1
            elif s2Count[leftChar] == s1Count[leftChar]:
                matches += 1
            s2Count[rightChar] = s2Count[rightChar] + 1
            if s2Count[rightChar] == s1Count[rightChar] + 1:
                matches -= 1
            elif s2Count[rightChar] == s1Count[rightChar]:
                matches += 1
            if matches == 26:
                return True
            l += 1
            r += 1
        return False

    def checkInclusionV2(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l, r = 0, 0
        s1Count = [0] * 26
        s2Count = [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
            r += 1

        matches = 0  # 需 26 個字母都對上
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        if matches == 26:
            return True

        while r < len(s2):
            leftCharIndex = ord(s2[l]) - ord('a')
            rightCharIndex = ord(s2[r]) - ord('a')
            # left char
            s2Count[leftCharIndex] = s2Count[leftCharIndex] - 1
            if s2Count[leftCharIndex] == s1Count[leftCharIndex] - 1:
                matches -= 1
            elif s2Count[leftCharIndex] == s1Count[leftCharIndex]:
                matches += 1
            # right char
            s2Count[rightCharIndex] = s2Count[rightCharIndex] + 1
            if s2Count[rightCharIndex] == s1Count[rightCharIndex] + 1:
                matches -= 1
            elif s2Count[rightCharIndex] == s1Count[rightCharIndex]:
                matches += 1

            if matches == 26:
                return True
            l += 1
            r += 1
        return False


solution = Solution()
s1 = "ab"
s2 = "eidbaooo"
s3 = "eidboaoo"
print(solution.checkInclusion(s1, s2))
print(solution.checkInclusion(s1, s3))
print(solution.checkInclusionV2(s1, s2))
print(solution.checkInclusionV2(s1, s3))
