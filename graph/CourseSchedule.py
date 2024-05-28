# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi]
# indicates that you must take course bi first if you want to take course ai.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
#

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
#
# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0,
# and to take course 0 you should also have finished course 1. So it is impossible.
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preTable = {}
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if not preTable[course]:
                return True
            visited.add(course)
            if course in preTable:
                for pre in preTable[course]:
                    if not dfs(pre):
                        return False
            visited.remove(course)
            preTable[course] = []  # 確定可以修完的課，後續不需要再檢查一次
            return True

        for c1, c2 in prerequisites:
            if c1 == c2:
                return False  # 先修是同一堂課，edge case
            l1 = preTable.get(c1, [])
            l2 = preTable.get(c2, [])
            l1.append(c2)
            preTable[c1] = l1
            preTable[c2] = l2

        if len(preTable) > numCourses:  # 超過要修的課，edge case
            return False

        for c in preTable.keys():
            if not dfs(c):
                return False
        return True

    # 運用 Topological sort
    def canFinishV2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preps = {i: [] for i in range(numCourses)}
        visited = set()   # 紀錄走過的節點
        path = set()  # 紀錄目前某課堂的修課的順序，(c -> c 的先修 -> ...)
        for c1, c2 in prerequisites:
            if c1 == c2:
                return False  # edge case
            preps[c1].append(c2)

        def dfs(c):
            if c in path:  # 表示兩堂課互相為先修
                return False
            if c in visited:  # 表示此課程的先修路線已走過
                return True
            visited.add(c)
            path.add(c)
            for prep in preps[c]:
                if not dfs(prep):
                    return False
            path.remove(c)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


sol = Solution()
# print(sol.canFinish(2, [[1, 0]]))  # True
# print(sol.canFinish(2, [[1, 0], [0, 1]]))  # False
# print(sol.canFinish(2, [[1, 2], [1, 3]]))  # False
# print(sol.canFinish(3, [[1, 2], [1, 3]]))  # True
# print(sol.canFinish(3, [[1, 2], [1, 3], [3, 1]]))  # False
print(sol.canFinishV2(2, [[1, 0]]))  # True
print(sol.canFinishV2(2, [[1, 0], [0, 1]]))  # False
print(sol.canFinishV2(2, [[0, 1], [1, 0]]))  # False
print(sol.canFinishV2(3, [[0, 1], [1, 2]]))  # True
print(sol.canFinishV2(3, [[0, 1], [0, 2], [2, 0]]))  # False
