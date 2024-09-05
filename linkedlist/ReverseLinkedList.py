# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev


sol = Solution()
first = ListNode(1)
sec = ListNode(2)
third = ListNode(3)
four = ListNode(4)
five = ListNode(5)
first.next = sec
sec.next = third
third.next = four
four.next = five


print(sol.reverseList(None))
cur = sol.reverseList(first)
print("reverse list: ")
while cur:
    print(cur.val)
    cur = cur.next
