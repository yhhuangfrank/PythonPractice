from typing import List


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        res = [-1] * len(queries)
        trie = Trie()
        i = 0
        for idx, (x, m) in sorted(enumerate(queries), key=lambda q: q[1][1]):
            # 確保存入 Trie 的都是 <= m 的數
            while i < len(nums) and nums[i] <= m:
                trie.add(nums[i])
                i += 1
            res[idx] = trie.max_xor(x)
        return res


class Trie:
    def __init__(self):
        self.root = {}

    def add(self, num: int):
        node = self.root
        # 題目最大到 10^9, 使用一個足夠的位元長度(30)來對齊
        for i in range(30, -1, -1):
            bit = (num >> i) & 1
            if bit not in node:
                node[bit] = {}
            node = node[bit]

    def max_xor(self, x: int):
        if not self.root:
            return -1 # 代表目前 Trie 內部的數都小於 m
        node = self.root
        res = 0
        for i in range(30, -1, -1):
            # 要找 XOR 最大的話，要嘗試找相反的數
            # 0 找 1, 1 找 0
            bit = (x >> i) & 1
            target = 1 - bit
            if target in node:
                # 存在，代表二進制表示中該位會標記為 1
                res |= (1 << i) # 將 1 向左移動 i 位，變成 mask，取 “|” 操作後標記特定位置為 1
                node = node[target]
            else:
                # 不存在，繼續往下，XOR 結果為 0
                node = node[bit]
        return res


sol = Solution()
print(sol.maximizeXor([0, 1, 2, 3, 4], [[3, 1], [1, 3], [5, 6]]))
print(sol.maximizeXor([5, 2, 4, 6, 6, 3], [[12, 4], [8, 1], [6, 3]]))
