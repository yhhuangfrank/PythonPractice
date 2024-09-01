# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
# Example1:
# Input: nums1 = [1, 3], nums2 = [2]
# Output: 2.00000
# Explanation: merged
# array = [1, 2, 3] and median is 2.
# Example2:
# Input: nums1 = [1, 2], nums2 = [3, 4]
# Output: 2.50000
# Explanation: merged
# array = [1, 2, 3, 4] and median is (2 + 3) / 2 = 2.5.
from typing import List


class Solution:
    # O(M+N) time
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return 0
        merge = [0] * (len(nums1) + len(nums2))
        l, r = 0, 0
        cur = 0
        while l < len(nums1) and r < len(nums2):
            if nums1[l] <= nums2[r]:
                merge[cur] = nums1[l]
                l += 1
            else:
                merge[cur] = nums2[r]
                r += 1
            cur += 1
        while l < len(nums1):
            merge[cur] = nums1[l]
            l += 1
            cur += 1
        while r < len(nums2):
            merge[cur] = nums2[r]
            r += 1
            cur += 1

        mid = (len(merge) - 1) // 2
        if len(merge) % 2 != 0:
            return merge[mid]
        else:
            return (merge[mid] + merge[mid + 1]) / 2

    # O(log(min(M,N)))
    # A: [1, 4, 7], B: [2, 3]
    # merge: [1, 2, 3, 4, 7]
    # A 左半部分： [1], B 左半部分[2]
    # A 右半部分： [4, 7], B 右半部分[3]
    def findMedianSortedArraysV1(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return 0
        total = len(nums1) + len(nums2)
        half = total // 2  # 將個數分半
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A  # 讓 A 作為比較少數量的 array
        l, r = 0, len(A) - 1

        # 分隔 A, B 找到 merge 後 array 左半部分
        while True:
            i = l + (r - l) // 2  # 定位 A 左半部分終點
            j = half - i - 2  # 定位 B 左半部分終點
            Aleft = A[i] if i >= 0 else float("-inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Aright = A[i + 1] if i + 1 < len(A) else float("inf")
            Bright = B[j + 1] if j + 1 < len(B) else float("inf")
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 != 0:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

    # O(len(M+N)log(len(M+N)))
    def findMedianSortedArraysV2(self, nums1: List[int], nums2: List[int]) -> float:
        merge = nums1 + nums2
        merge.sort()
        mid = (len(merge) - 1) // 2
        if len(merge) % 2 != 0:
            return merge[mid]
        else:
            return (merge[mid] + merge[mid + 1]) / 2


sol = Solution()
print(sol.findMedianSortedArrays([1, 3], [2]))
print(sol.findMedianSortedArrays([1, 2], [3, 4]))
print(sol.findMedianSortedArraysV1([1, 3], [2]))
print(sol.findMedianSortedArraysV1([1, 2], [3, 4]))
print(sol.findMedianSortedArraysV2([1, 3], [2]))
print(sol.findMedianSortedArraysV2([1, 2], [3, 4]))
