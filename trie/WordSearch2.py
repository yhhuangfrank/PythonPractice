from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        ROWS, COLS = len(board), len(board[0])
        resultSet = set()
        # construct Prefix Tree
        prefixTree = Trie()
        for word in words:
            prefixTree.addWord(word)
        # dfs run every combination on the board and test if it is in the tree
        visit = set()
        def dfs(r, c, node, word):
            if (
                min(r, c) < 0 or r == ROWS or c == COLS
                or (r, c) in visit
                or board[r][c] not in node.children
            ):
                return
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.word:
                resultSet.add(word)
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dfs(r + dr, c + dc, node, word)
            visit.remove((r, c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, prefixTree.root, "")

        return list(resultSet)
        

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True 

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
sol = Solution()
board1 = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
board2 = [["a","b"],["c", "d"]]
words1 = ["oath","pea","eat","rain"]
words2 = ["abcd"]
print(sol.findWords(board1, words1))
print(sol.findWords(board2, words2))
