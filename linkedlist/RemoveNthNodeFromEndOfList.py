# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
from typing import Optional


# Input: head = [1], n = 1
# Output: []

# Input: head = [1,2], n = 1
# Output: [1]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 掃過一次確認 list 長度
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        # 用 list 長度反過來計算正序是第幾個節點
        no_of_node = size - n + 1
        step = no_of_node - 1
        prev = ListNode(-1)  # dummy
        curr = head
        while step > 0:
            prev = curr
            curr = curr.next
            step -= 1
        prev.next = curr.next
        return prev.next if no_of_node == 1 else head  # 返回新 head 節點

    # one-pass solution
    def removeNthFromEndV2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 倒數第幾個，相當於一個 R 指針指向最後的 None，L 指針指向往前 n 個單位的位置
        dummy = ListNode(-1, head)  # dummy
        l, r = dummy, head
        diff = 0
        while diff < n:
            r = r.next  # r, l 拉開 n 單位
            diff += 1
        while r:
            l, r = l.next, r.next  # r, l 同步移動，直到 r 指向 None

        # 移除節點
        l.next = l.next.next
        return dummy.next  # 返回新 head 節點
