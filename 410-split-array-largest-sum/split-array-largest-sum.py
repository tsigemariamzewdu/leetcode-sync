class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def isvalid(mid):
            count=0
            i=0
            running=0
            while i<len(nums):
                if running+nums[i]<=mid:
                    running+=nums[i]
                    i+=1
                else:
                    count+=1
                    running=nums[i]
                    i+=1
            if count+1>k:
                return False
            return True
    
        low=max(nums)
        high=sum(nums)

        while low<=high:
            mid=(low+high)//2
            if isvalid(mid):
                high=mid-1
            else:
                low=mid+1
        return low
        