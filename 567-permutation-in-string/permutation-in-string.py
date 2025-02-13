from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        k=len(s1)
        counter_s1=Counter(s1)
        mydict=Counter(s2[:k])
        if  mydict==counter_s1:
                return True

        l=0
        for r in range(k,len(s2)):
            if  mydict==counter_s1:
                return True
            mydict[s2[l]]-=1
            mydict[s2[r]]+=1
            if  mydict==counter_s1:
                return True

            if mydict[s2[l]]==0:
                del mydict[s2[l]]
            l+=1
        return False
       
        

        