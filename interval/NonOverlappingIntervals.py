# Given an array of intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
#
# Example 1:
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
#
# Example 2:
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
#
# Example 3:
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
from typing import List


class Solution:
    # O(NlogN) time
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 先按照 start 排序，方便判斷是否有 overlap
        intervals.sort(key=lambda x: x[0])

        lastEnd = intervals[0][1]  # 比較起點
        count = 0
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s < lastEnd:  # 有 overlap
                count += 1
                lastEnd = min(lastEnd, e)  # 追蹤較小的 end，將 overlap 可能性最小化
            else:
                lastEnd = e  # 沒有重疊，直接更新為目前的 interval
        return count


sol = Solution()
arr1 = [[1, 2], [2, 3], [3, 4], [1, 3]]
arr2 = [[1, 2], [1, 2], [1, 2]]
arr3 = [[1, 2], [2, 3]]
print(sol.eraseOverlapIntervals(arr1))
print(sol.eraseOverlapIntervals(arr2))
print(sol.eraseOverlapIntervals(arr3))
