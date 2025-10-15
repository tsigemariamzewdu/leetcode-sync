class TrieNode:

    def __init__(self):
        self.children=[None for _ in range(26)]
        self.count=0
        self.is_end=False
class Trie:

    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        cur=self.root
        for char in word:
            idx=ord(char)-97
            if cur.children[idx] is None:
                cur.children[idx]=TrieNode()
            cur=cur.children[idx]
        cur.is_end=True
        cur.count+=1

    def collect(self):
        result=[]

        def dfs(node,path):
            if node is None:
                return
            if node.is_end:
                result.append(("".join(path),node.count))
            for i in range(26):
                if node.children[i]:
                    dfs(node.children[i],path+[chr(i+97)])
        dfs(self.root,[])
        return result

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        trieNode=Trie()
        for word in words:
            trieNode.insert(word)
        allwords=trieNode.collect()
        allwords.sort(key=lambda list: (-list[1],list[0]))
        return [w  for w,c in allwords[:k]]
        