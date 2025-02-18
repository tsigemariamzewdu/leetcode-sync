class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]

        prepro=[1]*(len(nums))
        sufpro=[1]*(len(nums)+1)

        prepro[0]=nums[0]
        for i in range(len(nums)):
            prepro[i]=prepro[i-1]*nums[i]
        prepro=[1]+prepro
        print(prepro)

        sufpro[len(nums)-1]=nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            sufpro[i]=sufpro[i+1]*nums[i]
        print(sufpro)
        
        for i in range(len(nums)):
            res.append(prepro[i]*sufpro[i+1])
        return res
        