class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if sum(nums)==0:
            return "0"
        
        str_nums=[0]*len(nums)
        for i in range(len(nums)):
            str_nums[i]=str(nums[i])
        str_nums.sort(key=lambda x : x*10,reverse=True)
        return "".join(str_nums)