# Example 1:
# Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
# Output: 1
# Explanation: You can either teach user 1 the second language or user 2 the first language.
#
# Example 2:
# Input: n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]
# Output: 2
# Explanation: Teach the third language to users 1 and 3, yielding two users to teach.
from typing import List


class Solution:
    # O(N * M) time, M = 要教的使用者, 最壞為 len(languages)
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        lang_sets = [set(l) for l in languages]  # 0-indexed
        user_count = len(lang_sets)
        teach_set = set()
        for u, v in friendships:
            u, v = u - 1, v - 1  # 0-indexed
            if not (lang_sets[u] & lang_sets[v]):
                # 兩個人沒有交集，代表不能溝通
                teach_set.add(u)
                teach_set.add(v)

        if not teach_set:
            return 0
        min_count = user_count
        for l in range(1, n + 1):
            # 已經會 l 的人
            count = 0
            for i in teach_set:
                if l in lang_sets[i]:
                    count += 1
            # 需要學習的人數，找到最小值
            need_learn = len(teach_set) - count
            min_count = min(min_count, need_learn)

        return min_count


sol = Solution()
print(sol.minimumTeachings(2, [[1], [2], [1, 2]], [[1, 2], [1, 3], [2, 3]]))
print(sol.minimumTeachings(3, [[2],[1,3],[1,2],[3]], [[1,4],[1,2],[3,4],[2,3]]))