class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n=len(mat)
        m=len(mat[0])

        if r*c!=n*m:
            return mat

        one_d=[0]*(n*m)
        for i in range(n):
            for j in range(m):
                index=i*m + j
                one_d[index]=mat[i][j]
        two_d=[[0]*c for _ in range(r)]
        for k in range(len(one_d)):
            two_d[k//c][k%c]=one_d[k]
        return two_d


        
        

       


        
        