class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                temp = ""
                while stack and stack[-1] != "[":
                    temp += stack.pop()
                stack.pop()
                numString = ""
                while stack and ord("1") <= ord(stack[-1]) <= ord("9"):
                    numString += stack.pop()
                num = int(numString[::-1])
                word = temp
                for _ in range(num - 1):
                    temp += word
                for j in range(len(temp) - 1, -1, -1):
                    stack.append(temp[j])
        res = ""
        for c in stack:
            res += c
        return res

sol = Solution()
print(sol.decodeString("3[a]2[bc]")) # aaabcbc
print(sol.decodeString("3[a2[c]]")) # accaccacc
print(sol.decodeString("2[abc]3[cd]ef")) # abcabccdcdcdef