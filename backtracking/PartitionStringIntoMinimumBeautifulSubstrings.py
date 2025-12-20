from typing import Any


class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        # 題目長度只有最多只有 15，可以使用 recursion
        def isPowerOfFive(substring: str) -> bool:
            num = 0
            base = 1
            for i in range(len(substring) - 1, -1, -1):
                num += base * int(substring[i])
                base *= 2
            while num > 1 and num % 5 == 0:
                num = num // 5
            return num == 1

        def dfs(start: int) -> int | float | Any:
            if start == len(s):
                return 0
            if s[start] == '0':
                return float('inf')
            min_count = float('inf')
            # 找尋所有可能的切點
            for i in range(start, len(s)):
                substring = s[start: i + 1]
                if isPowerOfFive(substring):
                    # 剩下字串可能的切分數
                    res = dfs(i + 1)
                    # 若剩下字串是可切分的
                    if res != float('inf'):
                        min_count = min(min_count, 1 + res)
            return min_count

        res = dfs(0)
        return -1 if res == float('inf') else res

# Example 1:
# Input: s = "1011"
# Output: 2
# Explanation: We can paritition the given string into ["101", "1"].
# - The string "101" does not contain leading zeros and is the binary representation of integer 51 = 5.
# - The string "1" does not contain leading zeros and is the binary representation of integer 50 = 1.
# It can be shown that 2 is the minimum number of beautiful substrings that s can be partitioned into.
#
# Example 2:
# Input: s = "111"
# Output: 3
# Explanation: We can paritition the given string into ["1", "1", "1"].
# - The string "1" does not contain leading zeros and is the binary representation of integer 50 = 1.
# It can be shown that 3 is the minimum number of beautiful substrings that s can be partitioned into.
#
# Example 3:
# Input: s = "0"
# Output: -1
# Explanation: We can not partition the given string into beautiful substrings.

sol = Solution()
print(sol.minimumBeautifulSubstrings("1011")) # 2
print(sol.minimumBeautifulSubstrings("111")) # 3
print(sol.minimumBeautifulSubstrings("0")) # -1