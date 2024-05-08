# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Example 3:
# Input: candidates = [2], target = 1
# Output: []
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def helper(i , currCombine, currSum):
            if i == len(candidates):
                if currCombine:
                    currCombine.pop()
                return
            if currSum == target:
                res.append(currCombine.copy())
                currCombine.pop()
                return
            if currSum > target:
                currCombine.pop()
                return
            
            if currSum < target:
                currCombine.append(candidates[i])
                helper(i, currCombine, currSum + candidates[i])
            helper(i + 1, currCombine, currSum)
            

        res = []
        helper(0, [], 0)
        return res
    

    # 更好解法
    def combinationSumV2(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(i, currCombine, currSum):
            if currSum == target:
                res.append(currCombine.copy())
                return
            if i == len(candidates) or currSum > target:
                return
            
            currCombine.append(candidates[i])
            dfs(i, currCombine, currSum + candidates[i])
            currCombine.pop()

            dfs(i + 1, currCombine, currSum)

        
        res = []
        dfs(0, [], 0)
        return res


sol = Solution()
print(sol.combinationSum([1,2,3], 3))
print(sol.combinationSum([2], 3))
print(sol.combinationSumV2([1,2,3], 3))
print(sol.combinationSumV2([2], 3))

