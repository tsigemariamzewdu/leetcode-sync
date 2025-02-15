from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums,k):
            count=0
            left=0
            unique=0
            mydict=defaultdict(int)

            for right in range(len(nums)):
                if mydict[nums[right]]==0:
                    unique+=1
                mydict[nums[right]]+=1

                while unique>k:
                    mydict[nums[left]]-=1
                    if mydict[nums[left]]==0:
                        unique-=1
                    left+=1
                count+=right-left+1
            return count
        return atMostK(nums,k)-atMostK(nums,k-1)
                
        