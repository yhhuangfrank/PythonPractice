# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
#
# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4
#
# Example 3:
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
from typing import List


class Solution:
    # brute force
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dfs(i):
            res = 1  # LIS 只有目前元素時，長度為一
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    res = max(res, 1 + dfs(j))
            return res

        return max(dfs(idx) for idx in range(len(nums)))

    # memoization
    def lengthOfLISV2(self, nums: List[int]) -> int:
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]
            res = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    res = max(res, 1 + dfs(j))
            cache[i] = res
            return cache[i]

        return max(dfs(idx) for idx in range(len(nums)))

    # DP - top down, O(n ^ 2) time
    def lengthOfLISV3(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)


sol = Solution()
arr1 = [10, 9, 2, 5, 3, 7, 101, 18]
arr2 = [0, 1, 0, 3, 2, 3]
arr3 = [7, 7, 7, 7, 7, 7, 7]
print(sol.lengthOfLIS(arr1))
print(sol.lengthOfLIS(arr2))
print(sol.lengthOfLIS(arr3))
print("=========================")
print(sol.lengthOfLISV2(arr1))
print(sol.lengthOfLISV2(arr2))
print(sol.lengthOfLISV2(arr3))
print("=========================")
print(sol.lengthOfLISV3(arr1))
print(sol.lengthOfLISV3(arr2))
print(sol.lengthOfLISV3(arr3))
