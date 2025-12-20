from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        max_num = 0
        n = len(customers)
        for i in range(n):
            if grumpy[i] == 0:
                max_num += customers[i]
        l, r = 0, 0
        temp = max_num
        while r < n:
            while r - l < minutes:
                if grumpy[r] == 1:
                    temp += customers[r]
                r += 1
            max_num = max(max_num, temp)
            if grumpy[l] == 1:
                temp -= customers[l]
            l += 1
        return max_num


# Example 1:
# Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
# Output: 16
#
# Explanation:
# The bookstore owner keeps themselves not grumpy for the last 3 minutes.
# The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
#
# Example 2:
# Input: customers = [1], grumpy = [0], minutes = 1
# Output: 1

sol = Solution()
print(sol.maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3)) # 16
print(sol.maxSatisfied([1], [0], 1)) # 1