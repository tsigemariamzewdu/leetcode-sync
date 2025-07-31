class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first={}
        last={}
        count={}
        for i,n in enumerate(nums):
            if n not in first:
                first[n]=i
            last[n]=i
            count[n]=count.get(n,0)+1
        
        res=len(nums)
        maxi=max(count.values())
        for i in count:
            if count[i]==maxi:
                res=min(res,last[i]-first[i]+1)
        return res
       
        