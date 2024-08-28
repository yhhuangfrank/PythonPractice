# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
from typing import List


class Solution:
    # O(logN) time
    def search(self, nums: List[int], target: int) -> int:
        def findMin():
            res = 0
            s, e = 0, len(nums) - 1
            while s <= e:
                if nums[e] >= nums[s]:
                    if nums[s] < nums[res]:
                        res = s
                    break
                m = s + (e - s) // 2
                if nums[m] < nums[res]:
                    res = m
                if nums[m] >= nums[s]:
                    s = m + 1
                else:
                    e = m - 1
            return res

        def binarySearch(s, e):
            while s <= e:
                m = s + (e - s) // 2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    e = m - 1
                else:
                    s = m + 1
            return -1

        # find index of min val in nums
        idx = findMin()
        # run binarySearch on both directions
        if nums[idx] == target:
            return idx
        start = 0
        end = 0 if idx - 1 < 0 else idx - 1
        left = binarySearch(start, end)
        if left != -1:
            return left
        start = len(nums) - 1 if idx + 1 == len(nums) else idx + 1
        end = len(nums) - 1
        return binarySearch(start, end)

    # O(logN) time
    def searchV2(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) - 1
        while s <= e:
            m = s + (e - s) // 2
            if nums[m] == target:
                return m
            # left sorted portion
            if nums[m] >= nums[s]:
                if nums[m] < target or nums[s] > target:
                    s = m + 1
                else:
                    e = m - 1
            # right sorted portion
            else:
                if nums[m] > target or nums[e] < target:
                    e = m - 1
                else:
                    s = m + 1
        return -1


sol = Solution()
arr1 = [4, 5, 6, 7, 0, 1, 2]
arr2 = [1]
print(sol.search(arr1, 0))  # 4
print(sol.search(arr1, 3))  # -1
print(sol.search(arr2, 0))  # -1
print(sol.search(arr2, 1))  # 0


print(sol.searchV2(arr1, 0))  # 4
print(sol.searchV2(arr1, 3))  # -1
print(sol.searchV2(arr2, 0))  # -1
print(sol.searchV2(arr2, 1))  # 0
