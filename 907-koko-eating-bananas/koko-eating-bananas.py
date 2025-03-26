class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isvalid(mid):
            count=0
            for i in range(len(piles)):
                if piles[i]>mid:
                    if piles[i]%mid==0:
                        count+=piles[i]//mid
                    else:
                        count+=(piles[i]//mid)+1
                else:
                    count+= 1
          
            if count<=h:
                return True
            return False
        

        low=1
        high=max(piles)

        while low<=high:
            mid=(low+high)//2
         
            if isvalid(mid):
                high=mid-1
            else:
                low=mid+1
        return low