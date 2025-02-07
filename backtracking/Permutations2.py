# Given a collection of numbers, nums, that might contain duplicates, 
# return all possible unique permutations in any order.
# 
# Example 1:
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# 
# Example 2:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

from typing import List


class Solution:
    # O(n * n!) time
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        counts = {n: 0 for n in nums}
        for n in nums:
            counts[n] += 1

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for k in counts.keys():
                if counts[k] > 0:
                    perm.append(k)
                    counts[k] -= 1
                    dfs()
                    perm.pop()
                    counts[k] += 1
        
        dfs()
        return res

sol = Solution()
nums1 = [1, 1, 2]
nums2 = [1, 2, 3]
print(sol.permuteUnique(nums1))
print(sol.permuteUnique(nums2))
