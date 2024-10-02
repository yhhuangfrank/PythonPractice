# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # 法一, BFS
    def serializeByBFS(self, root: TreeNode) -> str:
        """
        Encodes a tree to a single string.
        """
        if not root:
            return ""
        q = deque()
        q.append(root)
        res = ""
        levelCounts = []
        while q:
            size = len(q)
            levelCounts.append(size)
            for _ in range(size):
                node = q.popleft()
                res += str(node.val) if node else "N"
                res += ","
                if node:
                    q.append(node.left)
                    q.append(node.right)
        # record levels
        res += ":"
        for cnt in levelCounts:
            res += str(cnt)
            res += ","
        return res

    def deserializeByBFS(self, data: str) -> TreeNode:
        """
        Decodes your encoded data to tree.
        """
        if not data:
            return None
        nodes, levels = data.split(":")
        nodes = nodes[:-1].split(",")
        levels = levels[:-1].split(",")
        prev = deque()
        cur = deque()
        i, j = 0, 0
        root = None
        while i < len(nodes):
            end = i + int(levels[j])
            while i < end:
                node = TreeNode(int(nodes[i])) if nodes[i] != "N" else None
                cur.append(node)
                i += 1
            # first level
            if not prev:
                root = cur.popleft()
                prev.append(root)
                j += 1
                continue
            # not first level
            prevLen = len(prev)
            for _ in range(prevLen):
                prevNode = prev.popleft()
                if prevNode:
                    node1 = cur.popleft()
                    node2 = cur.popleft()
                    prevNode.left = node1
                    prevNode.right = node2
                    prev.append(node1)
                    prev.append(node2)
            j += 1
        return root

    # 法一, DFS
    def serializeByDFS(self, root: TreeNode) -> str:
        res = []

        # preorder
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserializeByDFS(self, data: str) -> TreeNode:
        vals = data.split(",")
        index = [0]

        def dfs():
            if vals[index[0]] == "N":
                index[0] += 1
                return None
            node = TreeNode(int(vals[index[0]]))
            index[0] += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5
code = Codec()
# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()

root = deser.deserializeByBFS(ser.serializeByBFS(node1))
root1 = deser.deserializeByDFS(ser.serializeByDFS(node1))
