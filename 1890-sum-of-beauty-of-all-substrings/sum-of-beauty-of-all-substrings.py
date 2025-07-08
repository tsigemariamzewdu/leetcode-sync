class Solution:
    def beautySum(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            countarr=[0]*26
            for j in range(i,len(s)):
                countarr[ord(s[j])-97]+=1
                mini=float("inf")
                for k in countarr:
                    if k:
                        mini=min(mini,k)
                count += max(countarr)-mini
                
        return count

        