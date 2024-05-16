# A triplet is an array of three integers. You are given a 2D integer array triplets,
# where triplets[i] = [ai, bi, ci] describes the ith triplet.
# You are also given an integer array target = [x, y, z] that describes the triplet you want to obtain.
#
# To obtain target, you may apply the following operation on triplets any number of times (possibly zero):
#
# Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become
# [max(ai, aj), max(bi, bj), max(ci, cj)].
# For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j]
# will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].
# Return true if it is possible to obtain the target triplet [x, y, z]
# as an element of triplets, or false otherwise.
#
# Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
# Output: true
# Input: triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
# Output: false
# Input: triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]
# Output: true
from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        flagI, flagJ, flagK = False, False, False
        for i, j, k in triplets:
            if i > target[0] or j > target[1] or k > target[2]:
                continue
            if i == target[0]:
                flagI = True
            if j == target[1]:
                flagJ = True
            if k == target[2]:
                flagK = True
            if flagI and flagJ and flagK:
                return True
        return False


sol = Solution()
print(sol.mergeTriplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]))
print(sol.mergeTriplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5]))
print(sol.mergeTriplets([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]))
