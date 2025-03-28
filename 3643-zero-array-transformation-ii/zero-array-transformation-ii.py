class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        numms=nums.copy()
       


        def isvalid(mid):
            diff=[0]*(len(nums)+2)

            for i in range(mid):
                l,r,x=queries[i]
                diff[l]+=x
                if r+1<len(diff):
                    diff[r+1]-=x
            curr=0
            flag=True
            for i in range(len(nums)):
                curr+=diff[i]
                if numms[i]-curr>0:
                    flag=False
                    break
            return flag     

        low=0
        high=len(queries)
        ans=-1
        

        while  low<=high:
            mid=(low+high)//2
            
            if isvalid(mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

        