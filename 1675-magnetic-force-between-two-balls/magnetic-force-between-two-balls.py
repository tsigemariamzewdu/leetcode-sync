class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        

        def isvalid(mid):
            count=1
            cur=position[0]
            for i in range(1,len(position)):
                if position[i]-cur>=mid:
                    count+=1
                    cur=position[i]
                    if count==m:
                        return True
            return False
            

           

        low=1
        high=(max(position)-min(position))

        while low<=high:
            mid=(low+high)//2


            if isvalid(mid):
                ans = mid
                low=mid+1
            else:
                high=mid-1
        return high
        