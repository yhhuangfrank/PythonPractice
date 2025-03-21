# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
# Example 1:
# Input: s = "()"
# Output: true
#
# Example 2:
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
# Input: s = "(]"
# Output: false

class Solution:
    def isValid(self, s: str) -> bool:
        opens = {"(", "{", "["}
        stack = []

        for c in s:
            if c in opens:
                stack.append(c)
                continue
            if not stack:
                return False
            # compare with popped element
            pop = stack.pop()
            if c == ")" and pop != "(":
                return False
            if c == "}" and pop != "{":
                return False
            if c == "]" and pop != "[":
                return False

        return False if stack else True


sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
