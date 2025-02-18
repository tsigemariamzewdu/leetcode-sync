class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefixfreq=[0]*(len(nums)+1)

        for s, e in requests:
            prefixfreq[s]+=1
            prefixfreq[e+1]-=1 
           

        prefixsum=[0]*len(nums)

        prefixsum[0]=prefixfreq[0]

        for i in range(1,len(prefixfreq)-1):
            prefixsum[i]=prefixsum[i-1] + prefixfreq[i]
        prefixsum.sort()
        nums.sort()

        result=0



        for j in range(len(prefixsum)):
            result += (nums[j]*prefixsum[j])
        return result%((10**9)+7)
            

        
        