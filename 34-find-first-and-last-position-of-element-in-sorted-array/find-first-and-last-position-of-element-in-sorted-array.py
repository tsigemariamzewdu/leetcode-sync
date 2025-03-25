class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result=[]


        left=0
        right=len(nums)-1
       
        while  left<=right:
            mid=(left+right)//2
           
            if nums[mid]>=target:
                right=mid-1
            else:
                left=mid+1
        if  left<len(nums) and nums[left]==target:
            result.append(left)
        else:
            result.append(-1)
        
        left=0
        right=len(nums)-1

        while  left<=right:
            mid=(left+right)//2
            if nums[mid]<=target:
                left=mid+1
            else:
                right=mid-1
        if right>-1 and nums[right]==target:
            result.append(right)
        else:
            result.append(-1)
       
        return result
        
        


        