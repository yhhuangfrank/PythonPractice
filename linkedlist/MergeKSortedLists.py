from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # O(NlogK) time
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(n1, n2):
            if not n1 and not n2:
                return None
            elif not n1:
                return n2
            elif not n2:
                return n1

            dummy = ListNode()
            cur = dummy
            l, r = n1, n2

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

        def helper(s, e):
            if e - s + 1 == 1:
                return lists[s]
            # divide into half until one linkedList
            m = s + (e - s) // 2
            return merge(helper(s, m), helper(m + 1, e))  # merge two linkedList

        return helper(0, len(lists) - 1) if lists else None


sol = Solution()
print(sol.mergeKLists([]))
print(sol.mergeKLists([None]))

l1 = ListNode(1)
l1.next = ListNode(4, ListNode(5))
l2 = ListNode(1)
l2.next = ListNode(3, ListNode(4))
l3 = ListNode(2, ListNode(6))
l4 = sol.mergeKLists([l1, l2, l3])

string = ""
node = l4
while node:
    string += str(node.val)
    if node.next:
        string += "->"
    node = node.next
print(string)
