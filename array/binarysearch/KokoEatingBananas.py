# Example 1:
# Input: piles = [3,6,7,11], h = 8
# Output: 4
#
# Example 2:
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
#
# Example 3:
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
from typing import List


class Solution:
    # O(NLog(Max(Piles))) time
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def calTime(n):
            res = 0
            for pile in piles:
                time = pile // n
                res += time if pile % n == 0 else time + 1
            return res

        # choose speed
        s, e = 1, max(piles)
        while s <= e:
            m = s + (e - s) // 2
            if calTime(m) > h:
                s = m + 1
            else:
                e = m - 1
        return e + 1


sol = Solution()
print(sol.minEatingSpeed(piles=[3, 6, 7, 11], h=8))  # 4
print(sol.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))  # 30
print(sol.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))  # 23
