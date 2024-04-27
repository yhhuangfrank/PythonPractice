# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
#
# There is only one repeated number in nums, return this repeated number.
#
# You must solve the problem without modifying the array nums and uses only constant extra space.
from typing import List


# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3

# Example 3:
# Input: nums = [3,3,3,3,3]
# Output: 3

class Solution:
    # 使用 set, O(n) time, O(n) space
    def findDuplicate(self, nums: List[int]) -> int:
        checkSet = set()
        for n in nums:
            if n in checkSet:
                return n
            checkSet.add(n)
        return -1

    # fast, slow two pointer + Floyd's algorithm
    # 依照 Floyd's algorithm，當找到 cycle 的第一次交會點時
    # 此時從起點另有一個 slow2, 當 slow 與 slow2 交會時即是 cycle 的起點
    def findDuplicateV2(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        # 找到第一次交會點
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if nums[fast] == nums[slow]:
                break
        # print(f"slow {slow}, fast {fast}, num {nums[slow]}")
        # 找到 cycle 的起點位置
        slow2 = 0
        while nums[slow2] != nums[slow]:
            slow2 = nums[slow2]
            slow = nums[slow]
        return nums[slow]


lst = [1, 3, 4, 2, 2]
solution = Solution()
print(solution.findDuplicateV2(lst))

m = {}
m[1] = 1
m[2] = 2
print(m)
m.pop(3)
