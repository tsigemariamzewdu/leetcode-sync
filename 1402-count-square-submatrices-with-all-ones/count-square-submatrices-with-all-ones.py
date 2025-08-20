class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n,m=len(matrix),len(matrix[0])
        res=0
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==1:
                    size=1
                    while i+size<=n and j+size<=m:
                        allones=True

                        for x in range(i,i+size):
                            for y in range(j,j+size):
                                if matrix[x][y]==0:
                                    allones=False
                                    break
                            if not allones:
                                break
                        if allones:
                            res+=1
                            size+=1
                        else:
                            break
        return res