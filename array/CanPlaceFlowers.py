# 給定一只有 0, 1 元素的 array，和一整數 n
# 0 代表此位置為空
# 1 代表此位置有種花
# n 代表有幾朵等待種植的花
# 每朵花必須間隔一個空位
# 問： 給定的 array 和 n 是否可將 n 朵花都種植
# 若可以全部種完回傳 true 否則回傳 false
# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
#
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:  # edge case
            return True

        remained = n
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                prev, post = max(i - 1, 0), min(i + 1, len(flowerbed) - 1)
                # 左右皆為空
                if flowerbed[prev] == 0 and flowerbed[post] == 0:
                    flowerbed[i] = 1
                    remained -= 1
            if remained == 0:
                return True
        return False


sol = Solution()
arr = [1, 0, 0, 0, 1]
print(sol.canPlaceFlowers(arr, 1))
print(sol.canPlaceFlowers(arr, 2))
