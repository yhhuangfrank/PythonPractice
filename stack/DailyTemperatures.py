# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to wait
# after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.
#
# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
#
# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
#
# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
from typing import List


class Solution:
    # O(n) time
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # monotonic-decreasing stack (單調遞減)
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1][0]] < t:
                idx, _ = stack.pop()
                res[idx] = i - idx
            stack.append((i, t))
        return res


sol = Solution()
arr1 = [73, 74, 75, 71, 69, 72, 76, 73]
arr2 = [30, 40, 50, 60]
arr3 = [30, 60, 90]
print(sol.dailyTemperatures(arr1))
print(sol.dailyTemperatures(arr2))
print(sol.dailyTemperatures(arr3))
