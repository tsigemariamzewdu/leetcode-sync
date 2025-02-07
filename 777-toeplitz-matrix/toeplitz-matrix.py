from collections import defaultdict
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        
        for r in range(rows):
            for c in range(cols):

                if r+1 <rows and c+1< cols and r-1 >=0 and c-1>=0:
                    if matrix[r][c]!=matrix[r+1][c+1] or matrix[r][c]!=matrix[r-1][c-1]:
                        return False
                elif r+1<rows and c+1<cols:
                    if matrix[r][c]!=matrix[r+1][c+1]:
                        return False
                elif r-1 >=0 and  c-1>=0:
                    if matrix[r][c]!=matrix[r-1][c-1]:
                        return False
                else:
                    continue
        return True

                


        