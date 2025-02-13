class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        maxlen=0
        zerolen=0

        for right in range(len(nums)):
            if nums[right]==0:
                zerolen+=1
            while zerolen>k:
                if nums[left]==0:
                    zerolen-=1
                left+=1
            maxlen=max(maxlen,right-left+1)
        return maxlen