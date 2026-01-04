from typing import List


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        res = []
        trie = Trie()
        for i, w in enumerate(wordsContainer):
            trie.addWord(w, i, len(w))
        for q in wordsQuery:
            idx = trie.query(q)
            res.append(idx)
        return res


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word, idx, length):
        self.update(self.root, idx, length)
        node = self.root
        # 使用反向遍歷紀錄 suffix
        for i in range(len(word) - 1, -1, -1):
            w = word[i]
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
            self.update(node, idx, length)

    # 每個節點上面的值，已經是該 suffix 的最佳 idx，直接返回
    def query(self, word):
        node = self.root
        for i in range(len(word) - 1, -1, -1):
            w = word[i]
            if w not in node.children:
                break
            node = node.children[w]

        return node.idx

    # 對於每個節點，update node idx and length
    def update(self, node, idx, length):
        if node.idx == -1:
            node.idx = idx
            node.length = length
        elif node.length > length:
            node.idx = idx
            node.length = length


class TrieNode:
    def __init__(self):
        self.idx = -1
        self.children = {}
        self.length = float('inf')

# Input: wordsContainer = ["abcd","bcd","xbcd"], wordsQuery = ["cd","bcd","xyz"]
# Output: [1,1,1]
# Input: wordsContainer = ["abcdefgh","poiuygh","ghghgh"], wordsQuery = ["gh","acbfgh","acbfegh"]
# Output: [2,0,2]

sol = Solution()
print(sol.stringIndices(["abcd", "bcd", "xbcd"], ["cd", "bcd", "xyz"])) # [1, 1, 1]
print(sol.stringIndices(["abcdefgh","poiuygh","ghghgh"], ["gh","acbfgh","acbfegh"])) # [2, 0, 2]
