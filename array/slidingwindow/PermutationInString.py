# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.
#
# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
#
# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

class Solution:
    # O(len(s1) * len(s2))
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count = {}
        for c in s1:
            count[c] = count.get(c, 0) + 1
        for s in range(len(s2)):
            temp = {}
            for e in range(s, s + len(s1)):
                if e >= len(s2):
                    break
                if s2[e] in count:
                    temp[s2[e]] = temp.get(s2[e], 0) + 1
            if self.checkSameFreq(count, temp):
                return True
        return False

    def checkSameFreq(self, map1, map2):
        for k in map1.keys():
            if k not in map2 or map1[k] != map2[k]:
                return False
        return True

    # O(len(s2)) time
    def checkInclusionV1(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l, r = 0, 0
        s1Count = [0] * 26
        s2Count = [0] * 26
        matches = 0

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1
            r += 1

        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
        if matches == 26:
            return True

        while r < len(s2):
            # left char
            lIndex = ord(s2[l]) - ord("a")
            s2Count[lIndex] -= 1
            if s2Count[lIndex] == s1Count[lIndex]:
                matches += 1
            elif s2Count[lIndex] + 1 == s1Count[lIndex]:  # 去掉之前是相同個數的
                matches -= 1
            # right char
            rIndex = ord(s2[r]) - ord("a")
            s2Count[rIndex] += 1
            if s2Count[rIndex] == s1Count[rIndex]:
                matches += 1
            elif s2Count[rIndex] - 1 == s1Count[rIndex]:  # 新增之前是相同個數的
                matches -= 1

            if matches == 26:
                return True
            l += 1
            r += 1
        return False


sol = Solution()
print(sol.checkInclusionV1("ab", "eidbaooo"))  # True
print(sol.checkInclusionV1("ab", "eidboaoo"))  # False
