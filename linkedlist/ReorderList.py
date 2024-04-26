# You are given the head of a singly linked-list. The list can be represented as:
#
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        prev = ListNode(-1)
        reverseHead = None
        for n in lst[::-1]:
            curr = ListNode(n)
            if reverseHead is None:
                reverseHead = curr
            prev.next = curr
            prev = curr

        # merge two list
        l = head
        r = reverseHead
        middle = self.findMiddle(reverseHead)
        lastR = None
        while r != middle:
            templ = l.next
            tempr = r.next
            l.next = r
            r.next = templ
            l = templ
            lastR = r
            r = tempr
        l.next = None
        if len(lst) % 2 == 0:
            lastR.next = None

    def findMiddle(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reorderListV2(self, head: Optional[ListNode]) -> None:
        middle = self.findMiddle(head)
        reverseHead = self.reverseList(middle.next)
        middle.next = None  # 斷開中心
        # merge two list
        l, r = head, reverseHead
        while r:
            tempL, tempR = l.next, r.next
            l.next = r
            r.next = tempL
            l, r = tempL, tempR

    def reverseList(self, head):
        if not head:
            return
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        return prev


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
one.next = two
two.next = three
three.next = four
Solution().reorderList(one)
