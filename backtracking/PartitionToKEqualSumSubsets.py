# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Input: nums = [1,2,3,4], k = 3
# Output: false
# 1 <= k <= nums.length <= 16
# 1 <= nums[i] <= 104

from typing import List


class Solution:
    # O(k^n) time
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        total = sum(nums)
        if total % k != 0: return False
        target = total / k
        nums.sort(reverse=True)
        sumSets = [0] * k

        def backtracking(i):
            if i == len(nums): return True
            for j in range(len(sumSets)):
                if sumSets[j] > target: continue
                sumSets[j] += nums[i]
                if backtracking(i + 1): return True
                sumSets[j] -= nums[i]
            return False

        return backtracking(0)
    # O(k * 2^N)
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        pass

sol = Solution()
print(sol.canPartitionKSubsets([4,3,2,3,5,2,1], 4))
print(sol.canPartitionKSubsets([1,2,3,4], 3))
