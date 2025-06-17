class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        bad=-1
        mini=-1
        maxi=-1

        result=0


        for i,n in enumerate(nums):

            if not minK<= n <= maxK:
                bad=i
            if minK==n:
                mini=i
            if maxK==n:
                maxi=i
            
            start=min(mini,maxi)

            if start>bad:
                result += (start-bad)
        return result