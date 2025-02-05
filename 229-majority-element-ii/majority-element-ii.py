from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result=[]
        counter=Counter(nums)
        for i in counter:
            if counter[i]>len(nums)//3:
                result.append(i)
        return result
        