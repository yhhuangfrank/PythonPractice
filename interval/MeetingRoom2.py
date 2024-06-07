# Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...]
# (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.
#
# Input: intervals = [(0,40),(5,10),(15,20)]
# Output: 2
# Explanation:
# day1: (0,40)
# day2: (5,10),(15,20)
#
# (0,8),(8,10) is not considered a conflict at 8
from typing import List


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    # 關鍵：找到最多同時有幾場 meeting 正在執行，就需要幾間 room
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]

        start.sort()
        end.sort()
        rooms, maxRooms = 0, 0
        i, j = 0, 0
        while i < len(intervals):
            if start[i] < end[j]:
                rooms += 1
                maxRooms = max(maxRooms, rooms)
                i += 1
            else:
                rooms -= 1
                j += 1
        return maxRooms


sol = Solution()
arr1 = [Interval(0, 40), Interval(5, 10), Interval(15, 20)]
arr2 = [Interval(0, 30), Interval(5, 10), Interval(10, 20)]
print(sol.minMeetingRooms(arr1))
print(sol.minMeetingRooms(arr2))
