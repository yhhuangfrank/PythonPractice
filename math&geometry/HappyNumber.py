# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
# 1. Starting with any positive integer, replace the number by the sum of the squares of its digits.
# 2. Repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# 3. Those numbers for which this process ends in 1 are happy.
#
# Return true if n is a happy number, and false if not.
#
# Example 1:
# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
#
# Example 2:
# Input: n = 2
# Output: false

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()  # 紀錄數字是否計算過
        temp = n

        while temp not in visited:
            visited.add(temp)
            square_sum = self.sum_of_squared(temp)
            if square_sum == 1:  # Happy number
                return True
            temp = square_sum
        # 重複計算了
        return False

    def sum_of_squared(self, num):
        square_sum = 0
        temp = num
        while temp != 0:
            digit = temp % 10
            square_sum += digit ** 2
            temp = temp // 10
        return square_sum


sol = Solution()
print(sol.isHappy(19))
print(sol.isHappy(2))
