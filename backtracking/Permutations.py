# Given an array nums of distinct integers,
# return all the possible permutations. You can return the answer in any order.
#
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
#
# Example 3:
# Input: nums = [1]
# Output: [[1]]
from typing import List


class Solution:
    # O(n^2 * n!) time
    def permute(self, nums: List[int]) -> List[List[int]]:
        # recursion
        def helper(i):
            if i == len(nums):
                return [[]]
            res = []
            # 遞迴取得前一次排列結果
            perms = helper(i + 1)
            for p in perms:
                # 選擇每個位置插入
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    res.append(pCopy)
            return res

        return helper(0)

    # O(n^2 * n!) time
    def permuteItertatively(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            newPerms = []
            for p in perms:
                for i in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(i, n)
                    newPerms.append(pCopy)
            perms = newPerms
        return perms


sol = Solution()
print(sol.permute([1, 2, 3]))
print(sol.permuteItertatively([1, 2, 3]))
