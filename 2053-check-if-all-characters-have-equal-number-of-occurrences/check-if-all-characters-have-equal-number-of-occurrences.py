from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter=Counter(s)
        valueint=counter[s[0]]
        for value in counter.values():
            if value!=valueint:
                return False
        return True
            

            

        
        