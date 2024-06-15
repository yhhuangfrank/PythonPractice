# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
import heapq
from typing import List


class Solution:
    # max heap, O(NlogN) time
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        for num, cnt in counter.items():
            heapq.heappush(maxHeap, (-cnt, num))

        res = []
        count = 0
        while maxHeap and count < k:
            cnt, num = heapq.heappop(maxHeap)
            res.append(num)
            count += 1
        return res

    # sort by count, O(NlogN) time
    def topKFrequentV2(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        elements = []
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        for num, cnt in counter.items():
            elements.append((cnt, num))

        elements.sort(key=lambda x: -x[0])
        res, count = [], 0
        while elements and count < k:
            res.append(elements[count][1])
            count += 1
        return res


sol = Solution()
print(sol.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
print(sol.topKFrequentV2(nums=[1, 1, 1, 2, 2, 3], k=2))
