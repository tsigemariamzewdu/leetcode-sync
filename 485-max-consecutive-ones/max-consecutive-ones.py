class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0
        currm=0
        for i in nums:
            if i==1:
                currm+=1
                maxi=max(maxi,currm)
            else:
                currm=0
        return maxi

        