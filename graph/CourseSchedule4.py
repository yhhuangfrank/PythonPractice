# CourseSchedule 系列題，多一組參數 queries，代表有多組 array [a,b]
# 檢查每個 array [a,b] 修 a 的課之前是否需要先修 b 課，並將每個 array 結果存入一個 list
#
# Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
# Output: [false,true]
# Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
# Course 0 is not a prerequisite of course 1, but the opposite is true.
# Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
# Output: [false,false]
# Explanation: There are no prerequisites, and each course is independent.
# Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
# Output: [true,true]
from typing import List


class Solution:
    # brute force
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:

        res = []
        preps = {i: [] for i in range(numCourses)}
        for c1, c2 in prerequisites:
            preps[c1].append(c2)

        def dfs(c1, c2):
            if c1 == c2:
                return True
            for prep in preps[c1]:
                if dfs(prep, c2):
                    return True
            return False

        for c1, c2 in queries:
            res.append(dfs(c1, c2))
        return res

    # optimal solution
    def checkIfPrerequisiteV2(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:
        res = []
        adj = {i: [] for i in range(numCourses)}
        total = {}  # 包含直接和間接為先修的課
        for c1, c2 in prerequisites:
            adj[c2].append(c1)

        def dfs(curr):
            if curr in total:
                return total[curr]
            s = set()
            for prep in adj[curr]:
                s.add(prep)
                for p in dfs(prep):
                    s.add(p)
            total[curr] = s
            return s

        for i in range(numCourses):
            dfs(i)
        for pre, c in queries:
            res.append(pre in total[c])
        return res


sol = Solution()
# print(sol.checkIfPrerequisite(2, [[1, 0]], [[0, 1], [1, 0]]))
print(sol.checkIfPrerequisiteV2(2, [[1, 0]], [[0, 1], [1, 0]]))
print(sol.checkIfPrerequisiteV2(2, [], [[0, 1], [1, 0]]))
print(sol.checkIfPrerequisiteV2(3, [[1, 2], [2, 0]], [[1, 2], [1, 0]]))
print(sol.checkIfPrerequisiteV2(6, [[3, 1], [3, 2], [4, 3], [5, 4], [5, 3]], [[5, 1], [4, 2]]))
