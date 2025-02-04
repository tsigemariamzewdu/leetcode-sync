from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        result=[]
        counter=Counter(nums)
        for i in counter:
            if counter[i]>1:
                result.append(i)
        return result
        