class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counter=Counter(nums)
        result=[]
        for i in counter:
            if counter[i]==2:
                result.append(i)
        return result

        