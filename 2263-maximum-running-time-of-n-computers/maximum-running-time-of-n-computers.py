class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        if len(batteries)<n:
            return 0
        tot=sum(batteries)
        low=0
        high=tot
        def valid(mid):
            count=0
            reserve=0
            for i in batteries:
                if i >=mid:
                    count+=1
                else:
                    reserve +=i
                    if reserve >=mid:
                        count+=1
                        reserve=reserve-mid
            return count >=n

                
        ans=0
        while low<=high:
            mid=(low+high)//2

            if valid(mid):
                ans=mid
                low =mid+1
            else:
                high=mid-1
        return ans

        