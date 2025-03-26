from bisect import bisect_left, bisect_right 
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]

        result=[]
        result.append(bisect_left(nums,target))
        result.append(bisect_right(nums,target)-1)


      
       
        return result
        
        


        