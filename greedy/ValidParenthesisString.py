# Given a string s containing only three types of characters: '(', ')' and '*',
# return true if s is valid.
#
# The following rules define a valid string:
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')'
#  or a single left parenthesis '(' or an empty string "".
#
# Example 1:
# Input: s = "()"
# Output: true
#
# Example 2:
# Input: s = "(*)"
# Output: true
#
# Example 3:
# Input: s = "(*))"
# Output: true

class Solution:
    # brute force
    def checkValidString(self, s: str) -> bool:
        symbols = ["", "(", ")"]
        sArr = list(s)
        stars = []
        for k in range(len(s)):
            if s[k] == "*":
                stars.append(k)

        def dfs(i, curr):
            if i == len(stars):
                return isValid(curr)

            for j in range(i, len(stars)):
                for symbol in symbols:
                    curr[stars[j]] = symbol
                    if dfs(j + 1, curr):
                        return True
                    curr[stars[j]] = "*"
            return False

        def isValid(arr):
            stack = []
            for val in arr:
                if val == "(":
                    stack.append(val)
                elif val == ")":
                    if not stack:
                        return False
                    stack.pop()
            return len(stack) == 0

        return dfs(0, sArr) if stars else isValid(sArr)

    # memoization O (n ^ 2)
    def checkValidStringV2(self, s: str) -> bool:
        # 由左至右看， "(" 的數量，必須要與")" 相同
        cache = {}

        def dfs(i, left):  # 代表 string index, 與 “(” 的數量
            if left < 0:
                return False
            if i == len(s):
                return left == 0  # 左右括號是否相同
            if (i, left) in cache:
                return cache[(i, left)]

            c = s[i]
            if c == "(":
                cache[(i, left)] = dfs(i + 1, left + 1)
            elif c == ")":
                cache[(i, left)] = dfs(i + 1, left - 1)
            else:
                cache[(i, left)] = (
                    dfs(i + 1, left) or dfs(i + 1, left + 1) or dfs(i + 1, left - 1)
                )
            return cache[(i, left)]

        return dfs(0, 0)

    # greedy (難想到)
    def checkValidStringV3(self, s: str) -> bool:
        # max 表示最多可有的"("數量
        # min 表示最低至少要有"("的數量
        leftMax, leftMin = 0, 0
        for c in s:
            if c == "(":
                leftMax, leftMin = leftMax + 1, leftMin + 1
            elif c == ")":
                leftMax, leftMin = leftMax - 1, leftMin - 1
            else:
                leftMax, leftMin = leftMax + 1, leftMin - 1
            if leftMax < 0:
                return False  # 最多可以有的“(” 不夠
            if leftMin < 0:
                leftMin = 0  # 下限
        return leftMin == 0  # 最終需等於 0


sol = Solution()
print(sol.checkValidStringV2("()"))
print(sol.checkValidStringV2("(*)"))
print(sol.checkValidStringV2("(*))"))
print(sol.checkValidStringV2("(*)("))






