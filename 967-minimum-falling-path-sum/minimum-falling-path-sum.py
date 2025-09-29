class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        for i in range(1,len(matrix)):
            for j in range(len(matrix)):
                left=matrix[i-1][j-1] if j!=0 else float("inf")
                mid=matrix[i-1][j]
                right=matrix[i-1][j+1] if j!=len(matrix[0])-1 else float("inf")

                matrix[i][j]+=min(left,right,mid)
        return min(matrix[-1])