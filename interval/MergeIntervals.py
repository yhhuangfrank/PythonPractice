# Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals, and return an array of the non-overlapping intervals
# that cover all the intervals in the input.
#
# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
#
# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
from typing import List


class Solution:
    # O(NlogN) time
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 透過 start 排序，方便判斷 interval 之間是否重疊
        intervals.sort(key=lambda x: x[0])
        res = []
        temp = intervals[0]

        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if temp[1] < s:
                res.append(temp)
                temp = [s, e]
            else:
                temp[0] = min(temp[0], s)
                temp[1] = max(temp[1], e)

        res.append(temp)
        return res


sol = Solution()
arr1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
arr2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16], [4, 8]]
print(sol.merge(arr1))
print(sol.merge(arr2))
