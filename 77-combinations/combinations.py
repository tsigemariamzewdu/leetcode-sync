class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]

        def backtrack(num,path):
            if len(path)==k:
                ans.append(path[:])
                return 
            
            for i in range(num,n+1):
                path.append(i)
                backtrack(i+1,path)
                path.pop()
        backtrack(1,[])
        return ans
            

      


        