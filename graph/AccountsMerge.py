from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # return self.accountsMerge1(accounts)
        return self.accountsMerge2(accounts)
    # DFS
    def accountsMerge1(self, accounts: List[List[str]]) -> List[List[str]]:
        emails = [] # 所有email
        emailIdx = {} # email -> idx
        emailToAcc = {} # email_idx -> account_id

        # 依照每個email整理對應的account
        idx = 0
        for accId, a in enumerate(accounts):
            for i in range(1, len(a)):
                email = a[i]
                # 不重複
                if email in emailIdx:
                    continue
                emails.append(email)
                emailIdx[email] = idx
                emailToAcc[idx] = accId
                idx += 1
        
        ### 串連同一account的email
        adj = [[] for _ in range(idx)]
        for a in accounts:
            # 有兩組email以上的互相串連
            for i in range(2, len(a)):
                idx1 = emailIdx[a[i]]
                idx2 = emailIdx[a[i - 1]]
                adj[idx1].append(idx2)
                adj[idx2].append(idx1)

        ### run DFS 遍歷所有email，整理到 accountToEmails
        accountToEmails = defaultdict(list)
        visited = [False] * idx

        def dfs(emailIdx, accId):
            visited[emailIdx] = True
            accountToEmails[accId].append(emails[emailIdx])
            # connected 的節點為同一account
            for neigh in adj[emailIdx]:
                if not visited[neigh]:
                    dfs(neigh, accId)
        
        for i in range(idx):
            if not visited[i]:
                dfs(i, emailToAcc[i])
        
        ### 整理為需求格式 List[[name, email1, email2, ...]]
        res = []
        for accId, emailList in accountToEmails.items():
            name = accounts[accId][0]
            lst = []
            lst.append(name)
            for email in sorted(emailList):
                lst.append(email)
            res.append(lst)
        return res
    
    # UnionFind
    def accountsMerge2(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        accToEmails = defaultdict(list)
        emailToAcc = {} # email -> account_id

        for accId, a in enumerate(accounts):
            for i in range(1, len(a)):
                email = a[i]
                if email in emailToAcc:
                    uf.union(emailToAcc[email], accId)
                else:
                    emailToAcc[email] = accId
        for email, accId in emailToAcc.items():
            parentId = uf.find(accId)
            accToEmails[parentId].append(email)
        
        res = []
        for accId, emailList in accToEmails.items():
            name = accounts[accId][0]
            lst = []
            lst.append(name)
            for email in sorted(emailList):
                lst.append(email)
            res.append(lst)
        return res

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    def find(self, n):
        p = self.parent[n]
        while p != self.parent[n]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[n]
        return p
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        r1, r2 = self.rank[p1], self.rank[p2]
        if r1 >= r2:
            self.parent[p2] = p1
            self.rank[p1] += r2
        elif r2 > r1:
            self.parent[p1] = p2
            self.rank[p2] += r1
        return True

# Input: accounts = 
# [
#     ["John","johnsmith@mail.com","john_newyork@mail.com"],
#     ["John","johnsmith@mail.com","john00@mail.com"],
#     ["Mary","mary@mail.com"],
#     ["John","johnnybravo@mail.com"]
# ]
# Output: [
#     ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
#     ["Mary","mary@mail.com"],
#     ["John","johnnybravo@mail.com"]
# ]

accounts = [
    ["John","johnsmith@mail.com","john_newyork@mail.com"],
    ["John","johnsmith@mail.com","john00@mail.com"],
    ["Mary","mary@mail.com"],
    ["John","johnnybravo@mail.com"]
]
sol = Solution()
print(sol.accountsMerge(accounts))
