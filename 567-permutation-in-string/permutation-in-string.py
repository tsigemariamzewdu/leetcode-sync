from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        firstdict=Counter(s1)
        n=len(s1)
        left=0
        right=n
        while right<=len(s2):
            windowCounter=Counter(s2[left:right])
            if firstdict==windowCounter:
                return True
            else:
                right+=1
                left+=1
        return False
        

        