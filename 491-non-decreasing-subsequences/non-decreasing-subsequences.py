class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res=set()

        path=[]

        def backtrack(start):
            nonlocal path
            if len(path)>=2:
                res.add(tuple(path[:]))
            for i in range(start,len(nums)):
                if not path or path[-1]<=nums[i]:
                    path.append(nums[i])
              
                    backtrack(i+1)
                    path.pop()
                # print(res)
        backtrack(0)
        return list(map(list, res)) 
        