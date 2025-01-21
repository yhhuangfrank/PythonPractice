class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
        
    def search(self, word: str) -> bool:
        
        def dfs(i, cur):
            if i == len(word):
                return cur.word
            # wildcard
            if word[i] == ".":
                # 每個 child 的 TrieNode 都嘗試
                for node in cur.children.values():
                    if dfs(i + 1, node):
                        return True
                return False
            # normal Trie search
            if word[i] not in cur.children:
                return False
            return dfs(i + 1, cur.children[word[i]])

        return dfs(0, self.root)
                
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

wordDictionary = WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
print(wordDictionary.search("pad")); # return False
print(wordDictionary.search("bad")); # return True
print(wordDictionary.search(".ad")); # return True
print(wordDictionary.search("b..")); # return True
