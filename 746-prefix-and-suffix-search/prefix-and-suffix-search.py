class TrieNode:
    def __init__(self):
        self.children=[None for _ in range(27)]
        self.idx=-1
       

class WordFilter:
    def __init__(self, words: List[str]):
        self.root=TrieNode()

        for i ,word in enumerate(words):
            wordd="{"+word
            for j in range(len(word)):
                w=word[j:]+wordd
                self.insert(w,i)


    def insert(self,word,index): 
        cur=self.root
        for char in word:
            i=ord(char)-97
            if cur.children[i] is None:
                cur.children[i]=TrieNode()
            cur=cur.children[i]
            cur.idx=index

    def f(self, pref: str, suff: str) -> int:
        cur=self.root
        word=suff+"{"+pref
        for char in word:
            i=ord(char)-97
            if cur.children[i] is None:
                return -1
            cur=cur.children[i]
        return cur.idx
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)