import copy
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n=len(mat)
        for _ in range(4):
            if mat==target:
                return True
            new_mat=[[0]*len(mat) for _ in range(len(mat))]
            for row in range(len(mat)):
                for col in range(len(mat)):
                    new_mat[col][n-1-row]=mat[row][col]
            mat=new_mat
        return False
                   
        
       
            
       