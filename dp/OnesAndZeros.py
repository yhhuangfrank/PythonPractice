# 給定一個二進位文字組成的 array，和兩個整數 m, n
# 找到用 array 元素組成的 subset 中最大的 subset，使得 subset 中最多 m 個 0 和 n 個 1
# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Input: strs = ["10","0","1"], m = 1, n = 1
# Output: 2
import time
from typing import List


class Solution:
    # brute force
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        countMap = {"0": 0, "1": 0}
        pairs = []
        for s in strs:
            for c in s:
                countMap[c] += 1
            pairs.append((countMap["0"], countMap["1"]))
            countMap["0"] = 0
            countMap["1"] = 0

        def dfs(i, pair):
            if i == len(strs):
                return 0
            # skip
            count = dfs(i + 1, pair)
            # include
            zeros, ones = pair
            newZeros, newOnes = zeros + pairs[i][0], ones + pairs[i][1]
            if newZeros <= m and newOnes <= n:
                newPair = (newZeros, newOnes)
                count = max(count, 1 + dfs(i + 1, newPair))
            return count

        return dfs(0, (0, 0))

    # memoization, O(m * n * s)
    def findMaxFormV2(self, strs: List[str], m: int, n: int) -> int:
        countMap = {"0": 0, "1": 0}
        pairs = []
        for s in strs:
            for c in s:
                countMap[c] += 1
            pairs.append((countMap["0"], countMap["1"]))
            countMap["0"] = 0
            countMap["1"] = 0
        cache = {}

        def dfs(i, pair):
            if i == len(strs):
                return 0
            if (i, pair) in cache:
                return cache[(i, pair)]
            # skip
            cache[(i, pair)] = dfs(i + 1, pair)
            # include
            zeros, ones = pair
            newZeros, newOnes = zeros + pairs[i][0], ones + pairs[i][1]
            if newZeros <= m and newOnes <= n:
                newPair = (newZeros, newOnes)
                cache[(i, pair)] = max(cache[(i, pair)], 1 + dfs(i + 1, newPair))
            return cache[(i, pair)]

        return dfs(0, (0, 0))

    # DP
    def findMaxFormV3(self, strs: List[str], m: int, n: int) -> int:
        countMap = {"0": 0, "1": 0}
        pairs = []
        for s in strs:
            for c in s:
                countMap[c] += 1
            pairs.append((countMap["0"], countMap["1"]))
            countMap["0"] = 0
            countMap["1"] = 0
        dp = {}
        for i in range(len(pairs)):
            for maxZero in range(m + 1):
                for maxOne in range(n + 1):
                    # skip
                    dp[(i, maxZero, maxOne)] = dp.get((i - 1, maxZero, maxOne), 0)
                    # include
                    if pairs[i][0] <= maxZero and pairs[i][1] <= maxOne:
                        newZeros, newOnes = maxZero - pairs[i][0], maxOne - pairs[i][1]
                        include = dp.get((i - 1, newZeros, newOnes), 0)
                        dp[(i, maxZero, maxOne)] = max(dp[(i, maxZero, maxOne)], 1 + include)
        return dp[(len(strs) - 1, m, n)]


sol = Solution()
strs1 = ["10", "0001", "111001", "1", "0"]
strs2 = ["10", "0", "1"]
strs3 = ["0", "11", "1000", "01", "0", "101", "1", "1", "1", "0", "0", "0", "0", "1", "0", "0110101", "0", "11", "01",
         "00", "01111", "0011", "1", "1000", "0", "11101", "1", "0", "10", "0111"]
# print(sol.findMaxForm(strs1, 5, 3))
# print(sol.findMaxForm(strs2, 1, 1))
t1 = time.time()
print(sol.findMaxFormV2(strs1, 5, 3))  # 4
print(sol.findMaxFormV2(strs2, 1, 1))  # 2
print(sol.findMaxFormV2(strs3, 9, 80))  # 17
t2 = time.time()
print(t2 - t1)

t1 = time.time()
print(sol.findMaxFormV3(strs1, 5, 3))
print(sol.findMaxFormV3(strs2, 1, 1))
print(sol.findMaxFormV3(strs3, 9, 80))
t2 = time.time()
print(t2 - t1)
