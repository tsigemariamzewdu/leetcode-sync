class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class Trie:

    def __init__(self):
        self.root=TrieNode()
        
    def insert(self, word: str) -> None:
        # if len(word)==1:
        #     cur.children[ord(word[0])-97]=TireNode()
        # else:
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

    
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trieNode=Trie()
        words.sort(key=lambda word: len(word))
        if len(words[0])>1:
            return ""
        maxi=float("-inf")
        res=words[0][0]
        for word in words:
            if len(word)==1:
                trieNode.insert(word)
            elif trieNode.search(word[:len(word)-1]) :
               
                trieNode.insert(word)
                maxi=max(maxi,len(word))
                if maxi==len(word):
                    if len(res)==len(word) and res > word:
                        res=word
                    elif len(word)>len(res):
                        res=word
                else:
                    if res > word:
                        res=word        
        return res
        

        