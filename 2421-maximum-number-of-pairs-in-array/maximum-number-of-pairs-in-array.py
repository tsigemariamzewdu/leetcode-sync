from collections import Counter
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        n=len(list(set(nums)))
        counteven=0
        cc=0
        counter=Counter(nums)
        for i in counter:
            if counter[i]%2==0:
                cc+=1
            
            counteven+=counter[i]//2
        return [counteven,n-cc]