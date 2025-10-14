class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class WordDictionary:

    def __init__(self):
        
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        cur=self.root
        for char in word:
            if cur.children[ord(char)-97] is None:
                cur.children[ord(char)-97]=TrieNode()
            cur=cur.children[ord(char)-97]
        cur.is_end=True
        

    def search(self, word: str) -> bool:
        
        def dfs(node,i):
            if node is None:
                return False
            if i==len(word):
                return node.is_end
            if word[i]==".":
                for ch in node.children:
                    if dfs(ch,i+1):
                        return True
            elif node.children[ord(word[i])-97] is not None:
                return dfs(node.children[ord(word[i])-97] , i+1)
            return False
        return dfs(self.root , 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)