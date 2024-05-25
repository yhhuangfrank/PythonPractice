# Given an integer array nums, return true if you can partition the array into two subsets
# such that the sum of the elements in both subsets is equal or false otherwise.
#
# Example 1:
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
# Example 2:
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
from typing import List


class Solution:
    # brute force
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        total = sum(nums)

        def dfs(i, currSum):
            if i == len(nums):
                return False
            if currSum == total - currSum:
                return True
            if dfs(i + 1, currSum + nums[i]) or dfs(i + 1, currSum):
                return True
            return False

        return dfs(0, 0)

    # memoization, O(n * sum(nums)) time, O(n * sum(nums)) space
    def canPartitionV2(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        cache = set()

        def dfs(i, currSum):
            if (i, currSum) in cache:
                return False
            if i == len(nums):
                return False
            if currSum == totalSum - currSum:
                return True
            if dfs(i + 1, currSum + nums[i]) or dfs(i + 1, currSum):
                return True
            cache.add((i, currSum))
            return False

        return dfs(0, 0)

    # DP - bottom up, O(n * sum(nums)) time, O(sum(nums)) space
    def canPartitionV3(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total / 2
        sumSet = set()  # 紀錄所有的 sum 可能
        sumSet.add(0)
        for i in range(len(nums) - 1, -1, -1):
            newSet = set(sumSet)
            for n in sumSet:
                if n == target or n + nums[i] == target:
                    return True
                newSet.add(n + nums[i])
            sumSet = newSet
        return False


sol = Solution()
arr1 = [1, 5, 11, 5]
arr2 = [1, 2, 3, 5]
# print(sol.canPartition(arr1))
# print(sol.canPartition(arr2))
# print(sol.canPartitionV2(arr1))
# print(sol.canPartitionV2(arr2))
print(sol.canPartitionV3(arr1))
print(sol.canPartitionV3(arr2))
