class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class Trie:

    def __init__(self):
        self.root=TrieNode()
        
    def insert(self, word: str) -> None:
        cur=self.root
        for char in word:
            if cur.children[ord(char)-97] is None:
                cur.children[ord(char)-97]=TrieNode()
            cur=cur.children[ord(char)-97]
        cur.is_end=True
        

    def search(self, word: str) -> bool:
        cur=self.root
        for char in word:
            if cur.children[ord(char)-97] is None:
                return False
            cur=cur.children[ord(char)-97]
        if cur.is_end:
            return True
        return False

    
    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for char in prefix:
            if cur.children[ord(char)-97] is None:
                return False
            cur=cur.children[ord(char)-97]
       
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)