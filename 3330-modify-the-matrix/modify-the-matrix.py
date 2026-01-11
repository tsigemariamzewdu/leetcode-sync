class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        res=[]
        for i in range(len(matrix[0])):
            newres=[]
            for j in range(len(matrix)):
                newres.append(matrix[j][i])
            for k in range(len(newres)):
                if newres[k] ==-1:
                    matrix[k][i]=max(newres)
            
        return matrix

            
                