# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
#
# Example 2:
# Input: s = "a"
# Output: [["a"]]
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(string):
            i, j = 0, len(string) - 1
            while i < j:
                if string[i] != string[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfs(i, curr):
            if i == len(s):
                res.append(curr.copy())
                return

            for j in range(i + 1, len(s) + 1):
                if is_palindrome(s[i:j]):
                    curr.append(s[i:j])
                    dfs(j, curr)
                    curr.pop()

        res = []
        dfs(0, [])
        return res


sol = Solution()
print(sol.partition("aab"))
print(sol.partition("a"))

l = []
print(len("".join(l)))

