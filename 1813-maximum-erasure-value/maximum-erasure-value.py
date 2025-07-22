class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
       
        ress=set()
        left=0
        maxi=0
        for right in range(len(nums)):
            while nums[right] in ress:
                ress.remove(nums[left])
                left+=1
            ress.add(nums[right])
            maxi=max(maxi,sum(ress))
                
                
                
            
        return max(maxi,sum(ress))

            

