class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        
        n=len(word)
        ans=0
        vowels={"a","e","i","o","u"}
        left=0
        seen=set()

        for right in range(n):
            if right>0 and word[right]<word[right-1]:
                seen.clear()
                left=right

            seen.add(word[right])
            if len(seen)==5:
                ans=max(ans,right-left+1)
        return ans

