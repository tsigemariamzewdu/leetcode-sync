class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans=[]
        path=[]

        def backtrack(i):
            if len(path)==k:
                ans.append(path[:])
                return 
            if i>n:
                return 
            
            path.append(i)
            backtrack(i+1)

            path.pop()
            backtrack(i+1)

        backtrack(1)
        return ans

        # def backtrack(num,path):
        #     if len(path)==k:
        #         ans.append(path[:])
        #         return

        #     for i in range(num,n+1):
        #         path.append(num)
        #         backtrack(num+1,path)
        #         path.pop()
        # backtrack(1,[])
        # return ans

        