# Given two non-negative integers num1 and num2 represented as strings,
# return the product of num1 and num2, also represented as a string.
#
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
#
# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"
#
# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"

class Solution:
    # O(len(num1) * len(num2)) time
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        n1 = num1[::-1]  # 反轉原有 str，方便計算每個位數
        n2 = num2[::-1]
        res = [0] * (len(num1) + len(num2))  # 相乘後位數最長為兩個數字的位數相加

        # 進行乘法
        for i in range(len(n2)):
            for j in range(len(n1)):
                num = int(n2[i]) * int(n1[j])
                res[i + j] += num
                res[i + j + 1] += res[i + j] // 10  # 處理進位
                res[i + j] = res[i + j] % 10

        # 輸出結果
        res = [str(val) for val in res][::-1]
        non_zero_index = 0
        while res[non_zero_index] == "0":
            non_zero_index += 1  # 忽略多餘的 "0"
        return "".join(res[non_zero_index:])


sol = Solution()
print(sol.multiply("2", "3"))
print(sol.multiply("123", "456"))
