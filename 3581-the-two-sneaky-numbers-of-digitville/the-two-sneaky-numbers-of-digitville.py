from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        counter=Counter(nums)
        for i in counter:
            if counter[i]>1:
                res.append(i)
        return res
        