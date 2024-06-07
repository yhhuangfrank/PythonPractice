from typing import List


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    # n ^ 2 time
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        inters = set()
        for interval in intervals:
            s, e = interval.start, interval.end
            if (s, e) in inters:
                return False
            for start, end in inters:
                if start == s and end < e:
                    return False
                if start < s < end:
                    return False
                if start < e < end:
                    return False
            inters.add((s, e))
        return True

    # O(n logn) time
    def canAttendMeetingsV2(self, intervals: List[Interval]) -> bool:
        # 先按照起始時間排序
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
        return True


sol = Solution()
arr1 = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
arr2 = [Interval(9, 15), Interval(5, 8)]
arr3 = [Interval(1, 2), Interval(1, 3)]
print(sol.canAttendMeetings(arr1))
print(sol.canAttendMeetings(arr2))
print(sol.canAttendMeetings(arr3))

print(sol.canAttendMeetingsV2(arr1))
print(sol.canAttendMeetingsV2(arr2))
print(sol.canAttendMeetingsV2(arr3))
