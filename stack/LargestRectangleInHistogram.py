# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1, return the area of the largest rectangle in the histogram.
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
#
# Input: heights = [2,4]
# Output: 4
from typing import List


class Solution:
    # O(N) time
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair of (index, height), index 代表該高度的長方形往左延伸可以作為起點位置
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                idx, h = stack.pop()
                maxArea = max(maxArea, (i - idx) * h)
                start = idx  # 當 pop 一個代表可以往回推一個起始位置
            stack.append((start, height))

        while stack:
            idx, h = stack.pop()
            maxArea = max(maxArea, (len(heights) - idx) * h)
        return maxArea

    # brute force, O(N^3) time, 固定寬
    def largestRectangleAreaV2(self, heights: List[int]) -> int:
        def findMinHeight(l, r):
            minH = heights[l]
            cur = l
            while cur <= r:
                minH = min(minH, heights[cur])
                cur += 1
            return minH

        maxArea = 0
        width = 1
        while width <= len(heights):
            for s in range(len(heights)):
                e = s + width - 1
                if e >= len(heights):
                    continue
                maxArea = max(maxArea, findMinHeight(s, e) * width)
            width += 1
        return maxArea

    # brute force, O(N^2) time, 固定高
    def largestRectangleAreaV3(self, heights: List[int]) -> int:
        def findMaxWidth(idx):
            l, r = idx, idx
            while l - 1 >= 0 and heights[l - 1] >= heights[idx]:
                l -= 1
            while r + 1 < len(heights) and heights[r + 1] >= heights[idx]:
                r += 1
            print(f'l: {l}, r: {r}')
            return r - l + 1

        maxArea = 0
        for i, h in enumerate(heights):
            maxArea = max(maxArea, findMaxWidth(i) * h)
        return maxArea


sol = Solution()
print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(sol.largestRectangleArea([2, 4]))
print(sol.largestRectangleArea([5, 2]))
print(sol.largestRectangleArea([1]))
#
# print(sol.largestRectangleAreaV3([2, 1, 5, 6, 2, 3]))
# print(sol.largestRectangleAreaV3([2, 4]))
# print(sol.largestRectangleAreaV3([5, 2]))
# print(sol.largestRectangleAreaV3([2, 1, 2]))
