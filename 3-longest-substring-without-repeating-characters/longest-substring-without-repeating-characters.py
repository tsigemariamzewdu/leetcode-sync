class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        candidate=set()
        maxlen=0
        while r<len(s):
            if s[r] not in candidate:
                candidate.add(s[r])
                r+=1
            else:
                while s[r] in candidate:
                    candidate.discard(s[l])
                    l+=1
            maxlen=max(maxlen,r-l)
                 
        if maxlen==0:
            return r
        return maxlen




    
        