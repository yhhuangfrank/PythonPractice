# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#
# Example 2:
# Input: nums = [0,1,1]
# Output: []
#
# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
from typing import List


class Solution:
    # O(NlogN) + O(N^2) = O(N^2) time
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # O(NlogN) time
        res = []

        for i, n in enumerate(nums):
            # 確保下一個不是重複的
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l, r = i + 1, len(nums) - 1
            target = -1 * nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l + 1] == nums[l]:
                        l += 1
                    l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return res


sol = Solution()
arr1 = [-1, 0, 1, 2, -1, -4]
arr2 = [0, 0, 0]
arr3 = [0, 1, 1]
arr4 = [0, 0, 0, 0]
print(sol.threeSum(arr1))
print(sol.threeSum(arr2))
print(sol.threeSum(arr3))
print(sol.threeSum(arr4))
