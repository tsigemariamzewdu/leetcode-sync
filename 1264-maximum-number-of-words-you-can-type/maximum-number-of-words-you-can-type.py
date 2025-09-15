class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count=0
        tempo=[]
        lists=text.split()
        broken=set(brokenLetters)
        for li in lists:
            flag=True
            for i in li:
                if i  in broken:
                    flag=False
            if flag:
                count+=1
        return count
                

       
        