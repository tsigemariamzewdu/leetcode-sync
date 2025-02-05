from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result=[]
        counter=Counter(nums)
        for i in counter:
            if counter[i]==2:
                result.append(i)
        return result


        