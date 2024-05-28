# CourseSchedule 的第二題，改成問: 修課順序
from typing import List


class Solution:
    # 此種 graph 排序主題與 Topological sort 相關
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        visited, resSet = set(), set()
        res = []

        def addCourse(course):
            if course not in resSet:
                resSet.add(course)
                res.append(course)

        def dfs(course):
            if course in visited:
                return False
            if not preMap[course]:
                addCourse(course)
                return True

            visited.add(course)
            for p in preMap[course]:
                if not dfs(p):
                    return False
            visited.remove(course)
            preMap[course] = []
            addCourse(course)
            return True

        if not prerequisites:
            return [i for i in range(numCourses)]
        for course, pre in prerequisites:
            if course == pre:
                return []
            preMap[course].append(pre)

        if len(preMap) > numCourses:
            return []

        for c in preMap:
            if not dfs(c):
                return []
        return res

    # 使用 Topological Sort
    def findOrderV2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visited, path = set(), set()
        preps = {i: [] for i in range(numCourses)}
        for c1, c2 in prerequisites:
            preps[c1].append(c2)

        def dfs(c):
            if c in path:
                return False
            if c in visited:
                return True
            visited.add(c)
            path.add(c)
            for prep in preps[c]:
                if not dfs(prep):
                    return False
            path.remove(c)
            res.append(c)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res


sol = Solution()
# print(sol.findOrder(2, [[1, 0]]))
# print(sol.findOrder(2, [[1, 0], [0, 1]]))
# print(sol.findOrder(4, [[1, 2], [1, 3]]))
# print(sol.findOrder(4, [[1, 2], [1, 3], [3, 1]]))
# print(sol.findOrder(4, []))
print(sol.findOrderV2(2, [[1, 0]]))
print(sol.findOrderV2(2, [[1, 0], [0, 1]]))
print(sol.findOrderV2(4, [[1, 2], [1, 3]]))
print(sol.findOrderV2(4, [[1, 2], [1, 3], [3, 1]]))
print(sol.findOrderV2(4, []))
