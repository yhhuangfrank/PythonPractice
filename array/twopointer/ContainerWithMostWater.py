# You are given an integer array height of length n.
# There are n vertical lines drawn such that
# the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container,
# such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.
#
#
# Example 1:
# Input:
# Output: 49
#
# Example 2:
# Input: height = [1,1]
# Output: 1
from typing import List


class Solution:
    # brute force, O(N^2) time
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                h = min(height[i], height[j])
                area = h * (j - i)
                maxA = max(maxA, area)
        return maxA

    # two pointer, O(N) time
    def maxAreaV2(self, height: List[int]) -> int:
        maxA = 0
        i, j = 0, len(height) - 1
        while i < j:
            hi, hj = height[i], height[j]
            area = min(hi, hj) * (j - i)
            maxA = max(maxA, area)
            if hi <= hj:
                i += 1
            else:
                j -= 1
        return maxA


sol = Solution()
arr1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
arr2 = [1, 1]
print(sol.maxArea(arr1))
print(sol.maxArea(arr2))
print(sol.maxAreaV2(arr1))
print(sol.maxAreaV2(arr2))
