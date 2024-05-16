# Given an array of integers nums and a positive integer k,
# check whether it is possible to divide this array into sets of k consecutive numbers.
# Return true if it is possible. Otherwise, return false.
# Example 1:
# Input: nums = [1,2,3,3,4,4,5,6], k = 4
# Output: true
# Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
#
# Example 2:
# Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
# Output: true
# Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
#
# Example 3:
# Input: nums = [1,2,3,4], k = 3
# Output: false
# Explanation: Each array should be divided in sub-arrays of size 3.
import heapq
from typing import List


# 與 HandOfStraights 相同
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]
            for i in range(first, first + k):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True


sol = Solution()
print(sol.isPossibleDivide([1, 2, 3, 3, 4, 4, 5, 6], 4))
print(sol.isPossibleDivide([3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3))
print(sol.isPossibleDivide([1, 2, 3, 4], 3))
