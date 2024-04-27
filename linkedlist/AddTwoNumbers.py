# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
from typing import Optional


# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        currL, currR = l1, l2
        carry = False
        dummy = ListNode(-1)
        curr = dummy
        # build result list
        while currL or currR or carry:
            l_val = currL.val if currL else 0
            r_val = currR.val if currR else 0
            sum_of_val = l_val + r_val
            if carry:
                sum_of_val += 1
            carry = sum_of_val >= 10  # 進位
            node = ListNode(sum_of_val % 10)
            curr.next = node
            curr = node
            currL = currL.next if currL else currL
            currR = currR.next if currR else currR
        return dummy.next
