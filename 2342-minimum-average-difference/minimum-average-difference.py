class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefix=[0]*(len(nums))
        res=[]
        prefix[0]=nums[0]
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]+nums[i]
        n=len(nums)
        
        for j in range(n-1):
            # print(prefix[j]//(j+1))
            # print((prefix[n-1]-prefix[j]))
            # print(n-j-1)
            res.append(abs((prefix[j]//(j+1))-(prefix[n-1]-prefix[j])//(n-j-1)))
        res.append(sum(nums)//n)
        mini=min(res)
        ans= res.index(mini)
        return ans
       
     


        

        