class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicate=set()
        r,l= 0,0
        result=0
        while r<len(s):
            while s[r] in duplicate:
                duplicate.remove(s[l])
                l+=1
            duplicate.add(s[r])
            r +=1
            result =max(result, r-l)
        return result
        