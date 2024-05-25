# 一 array，每個元素為一組 [a, b], a 代表身高, b 代表前面有 “幾個” 身高大於等於他的人
# 將 array 按此規則正確排序
# Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
# Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
# Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
from collections import deque
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 先按照身高大到小
        heightSet = set()
        table = {}
        for h, i in people:
            heightSet.add(h)
            table[h] = table.get(h, [])
            table[h].append(i)
        heights = list(heightSet)
        heights.sort(reverse=True)
        # 將每個高度的人按照"前方有多少個人"排序
        for k in table.keys():
            table[k].sort()
        # 再按照次序放到指定位置
        res = deque()  # linked list 特性，插入 O(1)
        for h in heights:
            for i in table[h]:
                res.insert(i, [h, i])
        return list(res)

    # 使用 lambda sort
    def reconstructQueueV2(self, people: List[List[int]]) -> List[List[int]]:
        copy = people.copy()
        copy.sort(key=lambda x: (-x[0], x[1]))
        res = deque()
        for h, i in copy:
            res.insert(i, [h, i])
        return list(res)


sol = Solution()
arr1 = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
arr2 = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
print(sol.reconstructQueue(arr1))
print(sol.reconstructQueue(arr2))
print(sol.reconstructQueueV2(arr1))
print(sol.reconstructQueueV2(arr2))
