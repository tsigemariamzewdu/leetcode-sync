class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        path=[]
        ans=[]
        def backtrack(idx):
            if sum(path[:])>target:
                return
            if sum(path[:])==target:
                val=sorted(path[:])
                if val in ans:
                    return 
                ans.append(val)
                return



            for i in range(len(candidates)):
                path.append(candidates[i])
                backtrack(idx+1)
                path.pop()
        backtrack(0)
        return ans
        
        
               