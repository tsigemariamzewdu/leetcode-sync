class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        fr="qwertyuiopQWERTYUIOP"
        sr="asdfghjklASDFGHJKL"
        tr="zxcvbnmZXCVBNM"
        result=[]

        for word in words:
            if word[0] in fr:
                cc=0
                for j in word:
                    if j in fr:
                        cc+=1
                if cc==len(word):
                    result.append(word)
            elif word[0] in sr:
                cc=0
                for j in word:
                    if j in sr:
                        cc+=1
                if cc==len(word):
                    result.append(word)
            elif word[0] in tr:
                cc=0
                for j in word:
                    if j in tr:
                        cc+=1
                if cc==len(word):
                    result.append(word)
        return result
                

            

            
        return words
        
        
        