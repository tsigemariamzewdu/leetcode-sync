class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        for num in range(2**(len(nums))):
            minires=[]

            for i in range(len(nums)):
            
                if num & (1<<i)!=0:
                    minires.append(nums[i])
            res.append(minires)
        return res
