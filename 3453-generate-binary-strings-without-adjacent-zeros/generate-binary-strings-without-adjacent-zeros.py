class Solution:
    def validStrings(self, n: int) -> List[str]:
        path=[]
        ans=[]

        def backtrack(idx):
            if len(path)==n:
                ans.append("".join(path[:]))
                return
            if idx>n:
                return 
            


        
        # recursive relation

            for i in ["0","1"]:
                if path and path[-1]=="0" and i=="0":
                    continue
                
                path.append(i)
                backtrack(idx+1)
                path.pop()
        backtrack(1)
        return ans

        