# Given n pairs of parentheses,
# write a function to generate all combinations of well-formed parentheses.
#
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
#
# Example 2:
# Input: n = 1
# Output: ["()"]
#
# 1 <= n <= 8
from typing import List


class Solution:
    # O(2^N) time
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(left, right, curr):
            if right > left:
                return
            if left == n and right == n:
                res.append("".join(curr.copy()))
                return
            if left < n:
                curr.append("(")
                dfs(left + 1, right, curr)
                curr.pop()
            if right < n:
                curr.append(")")
                dfs(left, right + 1, curr)
                curr.pop()

        dfs(0, 0, [])
        return res


sol = Solution()
print(sol.generateParenthesis(1))
print(sol.generateParenthesis(3))
