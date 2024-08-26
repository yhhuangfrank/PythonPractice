# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
#
# Example 2:
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
#
# Example 3:
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        s, e = 0, len(nums) - 1
        while s <= e:
            # when searching portion is already sorted
            if nums[e] >= nums[s]:
                res = min(res, nums[s])
                break
            # still rotated portion
            m = s + (e - s) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[s]:
                s = m + 1
            else:
                e = m - 1
        return res


sol = Solution()
arr1 = [3, 4, 5, 1, 2]
arr2 = [4, 5, 6, 7, 0, 1, 2]
arr3 = [11, 13, 15, 17]
print(sol.findMin(arr1))
print(sol.findMin(arr2))
print(sol.findMin(arr3))
