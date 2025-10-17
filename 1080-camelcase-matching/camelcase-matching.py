class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        cur=self.root
        for char in word:
            if char not in cur.children:
                cur.children[char]=TrieNode()
            cur=cur.children[char]
        

    def search(self,word,pattern):
        cur=self.root
        i=0
        n=len(pattern)
        for char in word:
            if char.isupper():
                if  i==n or char != pattern[i]:
                    return False
                else:
                    i+=1
                    cur=cur.children[char]
            else:
                if i<n and char==pattern[i]:
                    i+=1
                cur=cur.children[char]
        return i==n





class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        trieNode=Trie()
        for word in queries:
            trieNode.insert(word)
        result=[]
        for word in queries:
            result.append(trieNode.search(word,pattern))
        return result

        