import heapq
from typing import List


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        maxHeap = []  # (-1 * freq, val)
        n = len(nums)
        res = [0] * n
        freq_count = {}

        for i in range(n):
            val, f = nums[i], freq[i]
            if val not in freq_count:
                freq_count[val] = f
            else:
                freq_count[val] += f
            heapq.heappush(maxHeap, (-1 * freq_count[val], val))

            while maxHeap:
                top_freq, top_val = maxHeap[0]
                if top_freq == 0 or freq_count[top_val] != -1 * top_freq:
                    heapq.heappop(maxHeap)
                    continue
                break

            res[i] = -1 * maxHeap[0][0] if maxHeap else 0

        return res

sol = Solution()
print(sol.mostFrequentIDs([2, 3, 2, 1], [3, 2, -3, 1]))
print(sol.mostFrequentIDs([5, 5, 3], [2, -2, 1]))
