# You are given a string s. We want to partition the string into
# as many parts as possible so that each letter appears in at most one part.
#
# Note that the partition is done so that after concatenating all the parts in order,
# the resultant string should be s.
#
# Return a list of integers representing the size of these parts.
#
# Example 1:
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
#
# Example 2:
# Input: s = "eccbbbbdec"
# Output: [10]
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        parts, indexes = [], []  # 紀錄每個 part 與其最後 index 位置
        for i in range(len(s)):
            c = s[i]
            if not parts:
                stringSet = set()
                stringSet.add(c)
                parts.append(stringSet)
                indexes.append(i)
                continue
            isNeedMerged = False
            for j in range(len(parts) - 1, -1, -1):
                if c in parts[j]:
                    isNeedMerged = True
                    if j != len(parts) - 1:
                        newParts = self.merge(j, parts)
                        parts = newParts
                        # 重新整理 indexes
                        while len(indexes) > len(parts):
                            indexes.pop()
                    indexes[-1] = i
            if not isNeedMerged:
                newSet = set()
                newSet.add(c)
                parts.append(newSet)
                indexes.append(i)

        # 計算每個 part 字串大小
        res = []
        for i, size in enumerate(indexes):
            if i == 0:
                res.append(size + 1)
            else:
                res.append(size - indexes[i - 1])
        return res

    def merge(self, i, parts):
        newParts = []
        for j in range(i):
            newParts.append(parts[j])
        unionSet = set()
        for k in range(i, len(parts)):
            unionSet = unionSet.union(parts[k])
        newParts.append(unionSet)
        return newParts

    # greedy
    def partitionLabelsV2(self, s: str) -> List[int]:
        lastIndexMap = {}
        for i in range(len(s)):
            lastIndexMap[s[i]] = i

        res = []
        size, end = 0, 0
        for i in range(len(s)):
            end = max(end, lastIndexMap[s[i]])
            size += 1
            if i == end:
                res.append(size)
                size = 0
        return res


sol = Solution()
# print(sol.partitionLabels("eccbbbbdec"))
print(sol.partitionLabelsV2("eccbbbbdec"))
# print(sol.partitionLabels("ababcbacadefegdehijhklij"))
print(sol.partitionLabelsV2("ababcbacadefegdehijhklij"))
