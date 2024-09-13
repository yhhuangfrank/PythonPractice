# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
from collections import deque
from typing import List


class Solution:
    # O(n) time
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = deque()  # monotonic decreasing queue
        l, r = 0, 0

        while r < k:
            while window and window[-1] < nums[r]:
                window.pop()  # 從右側去除不需判斷的元素
            window.append(nums[r])
            r += 1
        res.append(window[0])

        while r < len(nums):
            while window and window[-1] < nums[r]:
                window.pop()
            window.append(nums[r])
            if nums[l] == window[0]:
                window.popleft()  # 去除最左邊(nums[l]已不在sliding window範圍內)
            res.append(window[0])
            l += 1
            r += 1
        return res


sol = Solution()
print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(sol.maxSlidingWindow([1], 1))
