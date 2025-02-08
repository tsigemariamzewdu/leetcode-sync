from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        forward=defaultdict(list)
        newres=[]
        rows=len(mat)
        cols=len(mat[0])

        for r in range(rows):
            for c in range(cols):
                forward[r+c].append(mat[r][c])
        count=0
        for i in forward:
            if count%2!=0:
                newres.extend(forward[i])
            else:
                forward[i].reverse()
                newres.extend(forward[i])
            count+=1
        return newres
        