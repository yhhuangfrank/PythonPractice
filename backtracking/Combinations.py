# Given two integers n and k,
# return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.

# Example 1:
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
#
# Example 2:
# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.
from typing import List


class Solution:
    # O(k * 2^n) time
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def helper(i, currCombine):
            if len(currCombine) == k:
                res.append(currCombine.copy())
                return
            if i == n + 1:
                return

            currCombine.append(i)
            helper(i + 1, currCombine)
            currCombine.pop()

            helper(i + 1, currCombine)

        helper(1, [])
        return res

    # O (k * C(n, k))
    def combineV2(self, n: int, k: int) -> List[List[int]]:
        res = []

        def helper(i, currCombine):
            if len(currCombine) == k:
                res.append(currCombine.copy())
                return
            if i == n + 1:
                return
            # 依序配對
            for j in range(i, n + 1):
                currCombine.append(j)
                helper(j + 1, currCombine)
                currCombine.pop()

        helper(1, [])
        return res


sol = Solution()
print(sol.combine(4, 2))
print(sol.combineV2(4, 2))
