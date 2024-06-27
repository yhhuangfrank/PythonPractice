# Example 1:
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
#
# Example 2:
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
#
# Example 3:
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []

        def calculate(x, y, operator):
            if operator == "+":
                return x + y
            elif operator == "-":
                return x - y
            elif operator == "*":
                return x * y
            else:
                return int(x / y)

        for token in tokens:
            if token in operators:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(calculate(n2, n1, token))
            else:
                stack.append(int(token))

        return stack[0]


sol = Solution()
arr1 = ["2", "1", "+", "3", "*"]
arr2 = ["4", "13", "5", "/", "+"]
arr3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

print(sol.evalRPN(arr1))
print(sol.evalRPN(arr2))
print(sol.evalRPN(arr3))


