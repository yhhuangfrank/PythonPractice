# House Robber 延伸，房子為環形排列 (第一間與最後一間相鄰)
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        rob1, rob2 = 0, 0
        # 從 0 ~ n - 2
        for i in range(len(nums) - 1):
            temp = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = temp
        first = rob2
        # 從 1 ~ n - 1
        for i in range(1, len(nums)):
            temp = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = temp
        second = rob2
        return max(first, second)
