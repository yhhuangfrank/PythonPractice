# Implement the LRUCache class:
#
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode(-1, -1)  # dummy
        self.tail = ListNode(-1, -1)  # dummy
        self.cache = {}  # map key to node
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1  # default value
        node = self.cache[key]
        res = node.val
        self.remove(node)
        self.insert(node)
        return res

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            node = ListNode(key, value)
            self.insert(node)
            self.cache[key] = node
        # check capacity
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.cache.pop(lru.key)
            self.remove(lru)

    # add from tail
    def insert(self, node):
        prev, tail = self.tail.prev, self.tail
        prev.next = node
        node.prev = prev
        node.next = tail
        tail.prev = node

    # remove from doubly linked list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev


class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
