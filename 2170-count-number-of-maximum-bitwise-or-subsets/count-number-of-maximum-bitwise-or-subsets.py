class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxi=0
        for i in nums:
            maxi |= i
        count=0
        res=[]
        path =[]

        def backtrack(start):
            nonlocal path
            res.append(path[:])
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
        backtrack(0)
        for lis in res:
            if lis:
                temp=0
                for k in lis:
                    temp|=k
                if temp==maxi:
                    count+=1
        return count

    

        

           
        