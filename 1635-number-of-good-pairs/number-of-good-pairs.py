class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter=Counter(nums)
        res=0

        for i in counter:
            if counter[i]>1:
                res += ( counter[i] *(counter[i]-1)//2)
        return res

        