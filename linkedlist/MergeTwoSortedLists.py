from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l, r = list1, list2
        dummy = ListNode()
        cur = dummy

        while l and r:
            if l.val <= r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next

        if l:
            cur.next = l
        if r:
            cur.next = r

        return dummy.next


sol = Solution()
lst1 = ListNode(1, ListNode(2, ListNode(3)))
lst2 = ListNode(1, ListNode(3, ListNode(4)))
node = sol.mergeTwoLists(lst1, lst2)
while node:
    print(node.val)
    node = node.next
