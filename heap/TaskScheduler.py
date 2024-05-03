# You are given an array of CPU tasks, each represented by letters A to Z, 
# and a cooling time, n. Each cycle or interval allows the completion of one task. 
# Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

# ​Return the minimum number of intervals required to complete all tasks.

# Input: tasks = ["A","A","A","B","B","B"], n = 2

# Output: 8

# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

# After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.
from typing import List
import heapq
from collections import deque

class Solution:
    # O (tasks * n)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count num of every letter in tasks
        count = {}
        for letter in tasks:
            count[letter] = count.get(letter, 0) + 1
        # build maxheap (process most frequent letter first, minimize idle time)
        max_heap = [-val for val in count.values()]
        heapq.heapify(max_heap)

        q = deque() # pairs of [-cnt, idleTime]
        time = 0
        while max_heap or q:
            time += 1
            if max_heap:
                val = -1 * heapq.heappop(max_heap)
                if val - 1 > 0:
                    next_time = time + n
                    q.append([val - 1, next_time])
            if q and q[0][1] == time:
                # can run task again
                popVal = q.popleft()[0]
                heapq.heappush(max_heap, -1 * popVal)
        return time
    

tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
sol = Solution()
print(sol.leastInterval(tasks, n))

