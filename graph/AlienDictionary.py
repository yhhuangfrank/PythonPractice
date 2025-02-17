# 新字典規則
# 字串 a, 字串 b，若字典中 a 排序比 b 小，須滿足其中一個條件：
# 1. a 與 b 的有一個字母不同
# 2. a字串長度 < b字串長度，且 a 為 b 的 prefix
# 給定一字串列，找出新字典中字母排序

from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for word in words:
            for c in word:
                if c not in adj:
                    adj[c] = set()
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            # w1 比 w2 長，且 w2 為 w1 的 prefix 時，不合乎規則
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                c1, c2 = w1[j], w2[j]
                if c1 != c2:
                    adj[c1].add(c2)
                    break
        
        visit = set()
        path = set()
        res = []

        # Topological Sort
        def dfs(node):
            if node in path:
                return False
            if node in visit:
                return True
            visit.add(node)
            path.add(node)
            for neigh in adj[node]:
                if not dfs(neigh):
                    return False
            path.remove(node)
            res.append(node)
            return True

        output = ""
        for c in adj.keys():
            if not dfs(c):
                return output
        
        for c in res[::-1]: # 反轉array(因為是post-order DFS)
            output += c
        return output
            