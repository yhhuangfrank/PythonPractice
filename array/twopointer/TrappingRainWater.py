# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.
# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented
# by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped.
#
# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9
from typing import List


class Solution:
    # O(n) time, O(n) memory
    def trap(self, height: List[int]) -> int:
        res = 0
        maxOnLeft = self.getMaxOnLeft(height)
        maxOnRight = self.getMaxOnRight(height)
        for i, h in enumerate(height):
            # find left, right boundary
            l, r = maxOnLeft[i], maxOnRight[i]
            # calculate max height of rain can be trapped
            maxH = min(l, r) - h
            if maxH > 0:
                res += maxH
        return res

    # O(n) time, O(1) memory, two pointer
    def trapV1(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0
        while l <= r:
            # 找到 bottleneck 的一邊
            if maxL <= maxR:
                if maxL - height[l] > 0:  # 計算可裝的水量
                    res += maxL - height[l]
                # update bottleneck
                maxL = max(maxL, height[l])
                l += 1
            else:
                if maxR - height[r] > 0:
                    res += maxR - height[r]
                maxR = max(maxR, height[r])
                r -= 1
        return res

    def getMaxOnLeft(self, arr):
        res = []
        curMax = 0
        for h in arr:
            curMax = max(curMax, h)
            res.append(curMax)
        return res

    def getMaxOnRight(self, arr):
        res = [0] * len(arr)
        curMax = 0
        for i in range(len(arr) - 1, -1, -1):
            curMax = max(curMax, arr[i])
            res[i] = curMax
        return res


sol = Solution()
arr1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
arr2 = [4, 2, 0, 3, 2, 5]
print(sol.trap(arr1))
print(sol.trap(arr2))
print(sol.trapV1(arr1))
print(sol.trapV1(arr2))
