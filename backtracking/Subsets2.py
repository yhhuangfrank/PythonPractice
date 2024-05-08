# Given an integer array nums that may contain duplicates, 
# return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. 
# Return the solution in any order.

# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
from typing import List


class Solution:
    # O(n * 2^n)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(i: int, currSet: List[int]) -> None:
            if i == len(nums):
                res.append(currSet.copy())
                return
            # 可能有多個元素的路線
            currSet.append(nums[i])
            dfs(i + 1, currSet)
            currSet.pop()

            # 跳過重複元素的路線
            j = i
            while j + 1 < len(nums) and nums[i] == nums[j + 1]:
                j += 1
            dfs(j + 1, currSet)

        # 先排列，讓重複的元素在左右。以避免選到重複元素
        # 排列不影響整體 time complexity
        nums.sort() 
        res = []
        dfs(0, [])
        return res


sol = Solution()
print(sol.subsetsWithDup([1,2,2]))
print(sol.subsetsWithDup([4,4,1,4]))
