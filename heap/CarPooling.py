import heapq
from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t : t[1]) # sort by starting point
        minHeap = []
        curPass = 0
        for numPass, start, end in trips:
            while minHeap and minHeap[0][0] <= start:
                curPass -= heapq.heappop(minHeap)[1]
            curPass += numPass
            if curPass > capacity: return False
            heapq.heappush(minHeap, [end, numPass])
        return True

sol = Solution()
print(sol.carPooling([[2,1,5],[3,3,7]], 4)) # False
print(sol.carPooling([[2,1,5],[3,3,7]], 5)) # True