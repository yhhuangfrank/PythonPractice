# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # two pass method
        old_to_new = {}  # map old node to new node
        curr = head
        while curr:
            new_node = Node(curr.val)
            old_to_new[curr] = new_node
            curr = curr.next
        # 第二次遍歷
        curr = head
        while curr:
            node = old_to_new[curr]
            nextNode = curr.next
            random = curr.random
            if nextNode in old_to_new:
                node.next = old_to_new[nextNode]
            if random in old_to_new:
                node.random = old_to_new[random]
            curr = curr.next
        return head if not head else old_to_new[head]
