import copy
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n=len(mat)
        if mat==target:
            return True
        for _ in range(4):
            for r in range(n):
                for c in range(r+1,n):
                    mat[r][c],mat[c][r]=mat[c][r],mat[r][c]
            for row in mat:
                row.reverse()
            if mat==target:
                return True
        return False


                   
        
       
            
       