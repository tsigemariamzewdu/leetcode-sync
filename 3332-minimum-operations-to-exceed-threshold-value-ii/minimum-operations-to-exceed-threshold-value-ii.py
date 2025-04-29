import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums.sort()
        
        heapq.heapify(nums)
        while not all(i >= k for i in nums):
 
            firstnum=nums[0]
            last=nums[-1]
            nums[0]=last
            heapq.heappop(nums)
            secondnum=nums[0]

            res= min(firstnum,secondnum) *2 + max(firstnum,secondnum)

            heapq.heappush(nums,res)
            secondlast=nums[-1]
            nums[0]=secondlast
            heapq.heappop(nums)
        return n-len(nums)



        