# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
# return the k closest points to the origin (0, 0).
#
# The distance between two points on the X-Y plane is the Euclidean distance
# (i.e., √(x1 - x2)2 + (y1 - y2)2).
#
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
#
# Example 1
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
#
# Example 2
# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.

import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # cluster same distance to the origin
        table = {}
        for x, y in points:
            distance = x ** 2 + y ** 2
            lst = table.get(distance, [])
            lst.append([x, y])
            table[distance] = lst

        distances = [dis for dis in table]
        heapq.heapify(distances)
        res = []
        while len(res) < k:
            if not distances:
                break
            distance = heapq.heappop(distances)
            for val in table[distance]:
                res.append(val)
        return res


