# Given an unsorted array of integers nums,
# return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
#
# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
#
# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0

        for n in numSet:
            if (n - 1) not in numSet:
                start = n
                length = 1
                while (start + 1) in numSet:
                    start += 1
                    length += 1
                maxLen = max(maxLen, length)
        return maxLen


sol = Solution()
arr1 = [100, 4, 200, 1, 3, 2]
arr2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(sol.longestConsecutive(arr1))
print(sol.longestConsecutive(arr2))
