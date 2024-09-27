# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
#
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
#
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        cur = head  # 遍歷的pointer
        count = 0
        dummy = ListNode(-1, head)
        lastTail = dummy  # 紀錄上一組的末端
        prev = cur  # 紀錄反轉前的 head
        while cur:
            if count == k:
                h, t = self.reverse(prev, k)
                lastTail.next = h
                lastTail = t
                prev = cur
                count = 0
            cur = cur.next
            count += 1

        # 若剛好再次為一組，進行反轉
        if count == k:
            h, t = self.reverse(prev, k)
            lastTail.next = h
            lastTail = t
            prev = cur
        lastTail.next = prev  # 將剩餘部分接上
        return dummy.next

    def reverse(self, node, k):
        count = 0
        prev = None
        cur = node
        while count < k:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count += 1
        return [prev, node]  # 返回反轉後的 head, tail


def printNode(node):
    cur = node
    res = ""
    while cur:
        res += (str(cur.val) + " -> ")
        cur = cur.next
    return res[:-4]

def prepare():
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3, ListNode(4, ListNode(5)))
    head.next = node1
    node1.next = node2
    return head


sol = Solution()
head = prepare()
node = sol.reverseKGroup(head, 2)
print(printNode(node))

head = prepare()
node = sol.reverseKGroup(head, 3)
print(printNode(node))
