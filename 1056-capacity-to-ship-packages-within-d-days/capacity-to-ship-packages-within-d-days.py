class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:



        def isValid(num):
            count=0

            i=0
            running=0

            while i<len(weights):
                if running+weights[i]<=num:
                    running+=weights[i]
                    i+=1
                else:
                    count+=1
                    running=weights[i]
                    i+=1
           
            if count+1>days:
                return False
            return True
            






        left=max(weights)
        right=sum(weights)

        while left<=right:
            mid=(left+right)//2
           
  
          

            if isValid(mid):
                right=mid-1
            else:
                left=mid+1
        return left
        