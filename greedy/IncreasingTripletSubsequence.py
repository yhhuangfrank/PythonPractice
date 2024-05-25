# Given an integer array nums, return true if there exists a triple of indices (i, j, k)
# such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
#
# Example 1:
# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
#
# Example 2:
# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
#
# Example 3:
# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
from typing import List


class Solution:
    # memoization
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        cache = set()

        def dfs(i):
            if i in cache:
                return 1
            res = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    res = max(res, 1 + dfs(j))
                    if res == 3:
                        return res
            cache.add(i)
            return res

        for i in range(len(nums)):
            if dfs(i) == 3:
                return True
        return False

    # DP - O(n^2) time
    def increasingTripletV2(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] == 3:
                        return True
        return False

    # greedy
    def increasingTripletV3(self, nums: List[int]) -> bool:
        minVal = float("inf")
        secMinVal = float("inf")

        for n in nums:
            if n <= minVal:
                minVal = n
            elif n <= secMinVal:
                secMinVal = n
            elif n > secMinVal:
                return True
        return False


sol = Solution()
arr1 = [2, 1, 5, 0, 4, 6]
arr2 = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1,
        2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2,
        1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1,
        2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2,
        1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1,
        2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print(sol.increasingTriplet(arr1))
print(sol.increasingTriplet(arr2))
print(sol.increasingTripletV2(arr1))
print(sol.increasingTripletV2(arr2))
print(sol.increasingTripletV3(arr1))
print(sol.increasingTripletV3(arr2))
