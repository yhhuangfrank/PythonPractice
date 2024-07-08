# There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
#
# You are given two integer array position and speed,
# both of length n, where position[i] is the starting mile of the ith car
# and speed[i] is the speed of the ith car in miles per hour.
#
# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
#
# A car fleet is a car or cars driving next to each other.
# The speed of the car fleet is the minimum speed of any car in the fleet.
#
# If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.
#
# Return the number of car fleets that will arrive at the destination.
#
# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Output: 3
#
# Explanation:
# The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
# The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
# The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6.
# The fleet moves at speed 1 until it reaches target.
from typing import List


class Solution:
    # O(NlogN) time, O(n) space
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(p, s) for p, s in zip(position, speed)]
        arr.sort(key=lambda x: x[0])  # 依照離 target 遠近排列(pos 由小到大)
        stack = []  # 依照時間單調遞增
        for p, s in arr[::-1]:  # 從距離終點近的開始遍歷
            time = (target - p) / s
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        return len(stack)


sol = Solution()
print(sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))  # 3
print(sol.carFleet(10, [3], [3]))  # 1
print(sol.carFleet(100, [0, 2, 4], [4, 2, 1]))  # 1
