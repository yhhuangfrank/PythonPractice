# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sum to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note: The solution set must not contain duplicate combinations.

# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#
# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
# [1,2,2],
# [5]
# ]
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(i, curr, currSum):
            if currSum == target:
                res.append(curr.copy())
                return
            if i == len(candidates) or currSum > target:
                return
            # 選擇至少一個目前的值路線
            curr.append(candidates[i])
            dfs(i + 1, curr, currSum + candidates[i])
            curr.pop()
            # 完全不選擇目前值的路線
            j = i
            while j + 1 < len(candidates) and candidates[i] == candidates[j + 1]:
                j += 1
            dfs(j + 1, curr, currSum)

        # 先排序
        candidates.sort()
        res = []
        dfs(0, [], 0)
        return res


sol = Solution()
print(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(sol.combinationSum2([2, 5, 2, 1, 2], 5))
