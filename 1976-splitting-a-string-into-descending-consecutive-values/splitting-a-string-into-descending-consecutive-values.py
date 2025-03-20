class Solution:
    def splitString(self, s: str) -> bool:
        n=len(s)
        current=[]
        def backtrack(idx):
            if idx>=len(s):
                for i in range(1,len(current)):
                    if current[i-1]-current[i]!=1:
                        return False
                return len(current)>=2






            for i in range(idx,n):
                val=int(s[idx:i+1])
                if current and  current[-1]-val!=1:
                    continue
                current.append(val)
                if backtrack(i+1):
                    return True
                current.pop()
            return False
        return backtrack(0)
            
           


        