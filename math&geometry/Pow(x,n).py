# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
#
# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000
#
# Example 2:
# Input: x = 2.10000, n = 3
# Output: 9.26100
#
# Example 3:
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
#
import time


class Solution:
    # brute force, O(n) time
    def myPow(self, x: float, n: int) -> float:

        def dfs(power):
            if power <= 1:
                return 1 if power == 0 else x
            return dfs(power - 1) * x

        if x == 0:
            return 0
        res = dfs(abs(n))
        return res if n >= 0 else 1 / res

    # cache, O(logN) time
    def myPowV2(self, x: float, n: int) -> float:
        cache = {0: 1, 1: x}  # 預設好 0, 1 次方數值

        def dfs(power):
            if power in cache:
                return cache[power]
            # divide and conquer
            if power % 2 == 0:
                cache[power] = dfs(power // 2) * dfs(power // 2)
            else:
                cache[power] = dfs((power - 1) // 2) * dfs((power - 1) // 2) * x
            return cache[power]

        if x == 0:
            return 0
        res = dfs(abs(n))
        return res if n >= 0 else 1 / res


sol = Solution()
t1 = time.time()
print(sol.myPow(2.000000, 900))
t2 = time.time()
diff1 = t2 - t1
print(f"brute force take {diff1} ms")

print("=================================")

t1 = time.time()
print(sol.myPowV2(2.000000, 900))
t2 = time.time()
diff2 = t2 - t1
print(f"cache method take {diff2} ms")
print(f"diff1 / diff2 is {diff1 / diff2}")
# print(sol.myPowV2(0.000001, 20000))
