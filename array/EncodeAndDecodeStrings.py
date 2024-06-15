# Design an algorithm to encode a list of strings to a single string.
# The encoded string is then decoded back to the original list of strings.
#
# Input: ["neet","code","love","you"] -> encode
# Output:["neet","code","love","you"] -> decode
#
# Input: ["we","say",":","yes"]
# Output: ["we","say",":","yes"]
#
# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.
from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "_" + s  # 組成編碼皆為： 長度 + _ + 原始字串
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            temp = i
            while s[temp] != "_":
                temp += 1
            length = int(s[i: temp])
            res.append(s[temp + 1: temp + 1 + length])
            i = temp + 1 + length
        return res


sol = Solution()
encode = sol.encode(["neet", "code", "love", "you"])
print(sol.decode(encode))
encode = sol.encode(["", "leet", "code", "_", ""])
print(sol.decode(encode))
encode = sol.encode(["1,23", "45,6", "7,8,9"])
print(sol.decode(encode))
