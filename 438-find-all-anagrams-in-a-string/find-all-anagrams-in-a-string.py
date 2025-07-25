from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target=Counter(p)

        k=len(p)
        l=0
        ans=[]
        if k>len(s):
            return ans
        mydict=Counter(s[:k])
        if mydict==target:
            ans.append(l)
        
        
        for r in range(k,len(s)):
            mydict[s[l]]-=1
            
            mydict[s[r]]+=1
            l+=1
            if mydict==target:
                ans.append(l)
            if mydict[s[l]]==0:
                del mydict[s[l]]
           
        return ans
            

            
        








        