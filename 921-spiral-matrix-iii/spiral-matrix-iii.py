class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        direction=[[0,1],[1,0],[0,-1],[-1,0]]
        res=[]
        r,c = rStart,cStart
        steps=1
        i=0
        while len(res)< rows * cols:
            for x in range(2):
                dr,dc=direction[i]
                for y in range(steps):
                    if (0<=r<rows and 0<=c< cols):
                        res.append([r,c])
                    r,c = r+dr, c+dc
                i =(i+1)%4 
                # we are doing this because we dont want i to be greater than 4
            steps +=1
        return res