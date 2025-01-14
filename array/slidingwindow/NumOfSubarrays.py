from typing import List

class Solution:
    # def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
    #     res = 0
    #     for l in range(len(arr) - k):
    #         currSum = 0
    #         for r in range(l, l + k):
    #             currSum += arr[r]
    #         if currSum >= threshold * k:
    #             res += 1
    #     return res
    def numOfSubarraysV2(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        currSum = 0
        res = 0

        for r in range(len(arr)):
            currSum += arr[r]
            if r - l + 1 < k:
                continue
            if currSum >= threshold * k:
                res += 1
            currSum -= arr[l]
            l += 1
        return res


arr1 = [2,2,2,2,5,5,5,8]
arr2 = [11,13,17,23,29,31,7,5,2,3]
sol = Solution()
# print(sol.numOfSubarrays(arr1, 3, 4))
# print(sol.numOfSubarrays(arr2, 3, 5))
# print(sol.numOfSubarraysV2(arr1, k=3, threshold=4)) # 3
# Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. 
# print(sol.numOfSubarraysV2(arr2, k=3, threshold=5)) # 6
