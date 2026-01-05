class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neglist=[]
        lists=[]
        zero=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]<0:
                    neglist.append(matrix[i][j]*-1)
                elif matrix[i][j]==0:
                    zero+=1
                else:
                    lists.append(matrix[i][j])
        # print(neglist)
        if len(neglist)%2==0 or zero>=1:
            return sum(lists)+ sum(neglist)
        
        else:
            lists.extend(neglist)

            
            return sum(lists) - 2 * min(lists)
