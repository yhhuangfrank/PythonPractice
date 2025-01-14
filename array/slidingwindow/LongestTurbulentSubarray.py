# Example 1:
# Input: arr = [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]

# Example 2:
# Input: arr = [4,8,12,16]
# Output: 2

# Example 3:
# Input: arr = [100]
# Output: 1

from typing import List

class Solution:
    # brute force, O(N^2) time
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        res = 1

        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                continue
            sign = 1 if arr[i] > arr[i + 1] else 0
            j = i + 1
            while j + 1 < len(arr):
                if arr[j] == arr[j + 1]:
                    break
                curSign = 1 if arr[j] > arr[j + 1] else 0
                if curSign == sign:
                    break
                sign = curSign
                j += 1
            res = max(res, j - i + 1)
        return res
    
    def maxTurbulenceSizeV2(self, arr: List[int]) -> int:
        l, r = 0, 1
        res, prev = 1, ""

        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1) # 結算
                r += 1
                prev = ">"
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            else:
                r = r + 1 if arr[r - 1] == arr[r] else r
                l = r - 1
                prev = ""
        return res

arr = [9,4,2,10,7,8,8,1,9]
sol = Solution()
print(sol.maxTurbulenceSize(arr))