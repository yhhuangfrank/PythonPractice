from typing import List 

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj = {}
        for src, dst in tickets:
            lst1 = adj.get(src, [])
            lst2 = adj.get(dst, [])
            lst1.append(dst)
            adj[src] = lst1
            adj[dst] = lst2

        for lst in adj.values():
            lst.sort(reverse=True)
        res = []

        def dfs(node):
            while adj[node]:
                dst = adj[node].pop()
                dfs(dst)
            res.append(node)     
        
        dfs("JFK")
        return res[::-1]
        
sol = Solution()
arr = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
arr1 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(sol.findItinerary(arr)) # ["JFK","MUC","LHR","SFO","SJC"]
print(sol.findItinerary(arr1)) # ["JFK","ATL","JFK","SFO","ATL","SFO"]

