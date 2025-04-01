class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
    

        ans=[]
       
        matrix=[["."]* n for _ in range(n)]
        colu=set()
       

        diag=set()
        antidiag=set()
        def backtrack(idx):
            if idx==n:
                val=[''.join(i) for i in matrix]
                ans.append(val)
                return


            for col in range(n):
                if col in colu or (idx+col) in diag or (idx-col) in antidiag:
                    continue
                else:
                    colu.add(col)
                    diag.add(idx+col)
                    antidiag.add(idx-col)
                    matrix[idx][col]="Q"
                    backtrack(idx+1)
                    colu.remove(col)
                    diag.remove(idx+col)
                    antidiag.remove(idx-col)
                    matrix[idx][col]="."
                    
        backtrack(0)
        return ans

                   


            









              