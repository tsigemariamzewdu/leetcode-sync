class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def isvalid(mid):
          
            count=0
            for i in range(len(candies)):
                if mid!=0:
                   
                    count+=candies[i]//mid
           
            return count>=k







        low=1
        high=max(candies)

        while low<=high:
            mid=(low+high)//2
            if isvalid(mid):
                low=mid+1
            else:
                high=mid-1
        return high
        