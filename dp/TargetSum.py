# You are given an integer array nums and an integer target.
#
# You want to build an expression out of nums by adding one of the symbols '+' and '-'
# before each integer in nums and then concatenate all the integers.
#
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1
# and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.
#
# Example 1:
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
#
# Example 2:
# Input: nums = [1], target = 1
# Output: 1
import time
from typing import List


class Solution:
    # brute force, O(2^n)
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def dfs(i, curr):
            if i == len(nums):
                return 1 if curr == target else 0
            return dfs(i + 1, curr + nums[i]) + dfs(i + 1, curr - nums[i])

        return dfs(0, 0)

    # memoization, O(n * sum(nums))
    def findTargetSumWaysV2(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(i, curr):
            if (i, curr) in cache:
                return cache[(i, curr)]
            if i == len(nums):
                return 1 if curr == target else 0

            cache[(i, curr)] = dfs(i + 1, curr + nums[i]) + dfs(i + 1, curr - nums[i])
            return cache[(i, curr)]

        return dfs(0, 0)


sol = Solution()
arr1 = [1, 1, 1, 1, 1]
arr2 = [48, 9, 50, 48, 38, 34, 47, 8, 1, 44, 27, 42, 45, 25, 23, 40, 6, 39, 21, 48]
t1 = time.time()
print(sol.findTargetSumWays(nums=arr1, target=3))
for _ in range(10):
    sol.findTargetSumWays(nums=arr2, target=29)
t2 = time.time()
print(t2 - t1)
t1 = time.time()
print(sol.findTargetSumWaysV2(nums=arr1, target=3))
for _ in range(10):
    sol.findTargetSumWaysV2(nums=arr2, target=29)
t2 = time.time()
print(t2 - t1)
