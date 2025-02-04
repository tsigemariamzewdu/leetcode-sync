class Solution:
    def printVertically(self, s: str) -> List[str]:
        words=s.split(" ")
        #["how","are","you"]
        max_word=0
        for i in words:
            if len(i)>max_word:
                max_word=len(i)
        #3
        
        result=[]
        for j in range(max_word): 
            stringg=[] 
            count=0
            for index in range(len(words)):
                    
                
                if len(words[index])>j:
                    stringg.append(words[index][j])
                else:
                    stringg.append(" ")
                
            count+=1
            strr="".join(stringg)
            result.append(strr.rstrip())
                    
            

                
                    
        return result


        