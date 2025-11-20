class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        place=-1
        for i in range(len(nums)):
            if nums[i] ==1:
                if place !=-1 and i-place-1 <k:
                    return False
                
                place = i
        return True

        