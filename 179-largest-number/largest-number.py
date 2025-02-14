class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if sum(nums)==0:
            return "0"
        str_nums=[]
        for i in nums:
            str_nums.append(str(i))
        str_nums.sort(key =lambda x: x*10,reverse=True)
        return "".join(str_nums)