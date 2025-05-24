class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zerosrow=set()
        zeroscol=set()
      
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    zerosrow.add(i)
                    zeroscol.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zerosrow or j in zeroscol:
                    matrix[i][j]=0


        



        