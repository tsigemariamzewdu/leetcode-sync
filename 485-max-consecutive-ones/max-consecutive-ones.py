class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0
        currmax=0
        for i in nums:
            if i==1:
                currmax+=1
                maxi=max(maxi,currmax)
            else:
                currmax=0
        return maxi

        