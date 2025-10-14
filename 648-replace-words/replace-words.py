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
        

    def search(self, word: str) -> str:
        cur=self.root
        res=[]
        for char in word:
            if cur.children[ord(char)-97] is None:
                return ""
            cur=cur.children[ord(char)-97]
            res.append(char)
            if cur.is_end:
                return "".join(res)
        return ""

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ans=[]
        trieNode=Trie()
        for word in dictionary:
            trieNode.insert(word)
        for w in sentence.split():
            if not trieNode.search(w):
                ans.append(w)
            else:
                ans.append(trieNode.search(w))
        return " ".join(ans)
            

        