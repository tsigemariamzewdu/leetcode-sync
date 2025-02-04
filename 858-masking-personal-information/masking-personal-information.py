class Solution:
    def maskPII(self, s: str) -> str:
        
        if s[0].isalpha():
            s=s.lower()
            for i,v in enumerate(s):
                if v=="@":
                    indexat=i
                    return s[0]+"*****"+s[i-1]+s[i:]



            
        else:
            newphone=''
            for i in s:
                if i.isdigit():
                    newphone+=str(i)
            if len(newphone)==10:
                return "***"+"-"+"***"+"-"+newphone[6:]
            if len(newphone)==11:
                return "+*"+"-"+"***"+"-"+"***"+"-"+newphone[7:]
            if len(newphone)==12:
                return "+**"+"-"+"***"+"-"+"***"+"-"+newphone[8:]
            if len(newphone)==13:
                return "+***"+"-"+"***"+"-"+"***"+"-"+newphone[9:]
            

            

        
        


        