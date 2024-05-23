# Given an integer array nums, find a subarray that has the largest product,
# and return the product.
#
# The test cases are generated so that the answer will fit in a 32-bit integer.
#
# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
from typing import List


class Solution:
    # brute force
    def maxProduct(self, nums: List[int]) -> int:
        maxVal = -float("inf")

        for i in range(len(nums)):
            curr = 1
            for j in range(i, len(nums)):
                curr *= nums[j]
                maxVal = max(maxVal, curr)
        return maxVal

    # DP - O(n) time
    def maxProductV2(self, nums: List[int]) -> int:
        res = -float("inf")
        currMax, currMin = 1, 1
        for n in nums:
            temp = currMax
            currMax = max(temp * n, currMin * n, n)
            currMin = min(temp * n, currMin * n, n)
            res = max(res, currMax)
        return res


sol = Solution()
arr1 = [2, 3, -2, 4]
arr2 = [-2, 0, -1]
print(sol.maxProduct(arr1))
print(sol.maxProduct(arr2))
print(sol.maxProductV2(arr1))
print(sol.maxProductV2(arr2))
