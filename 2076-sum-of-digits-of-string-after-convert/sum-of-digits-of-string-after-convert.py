class Solution:
    def getLucky(self, s: str, k: int) -> int:
        result=""
        for i in s:
            result+= str(ord(i)-96)
        
        for i in range(k):
    
            summ=0
            
            for i in result:
               summ += int(i)
               result=str(summ)
       

        return summ
            
        
        