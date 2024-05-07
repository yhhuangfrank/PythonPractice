# Given an integer array nums of unique elements, return all possible
# subsets
#  (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
from typing import List


class Solution:
    # O(n*2^n) time, O(n) space
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(i, curr):
            if i == len(nums):
                res.append(curr.copy())
                return
            # 選擇目前的數
            curr.append(nums[i])
            helper(i + 1, curr)
            curr.pop()  # 回溯

            # 不選擇目前的數
            helper(i + 1, curr)

        helper(0, [])
        return res


sol = Solution()
print(sol.subsets([1, 2, 3]))
