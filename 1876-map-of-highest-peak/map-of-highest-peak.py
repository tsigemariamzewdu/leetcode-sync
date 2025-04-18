class Solution:
    def highestPeak(self, mat: List[List[int]]) -> List[List[int]]:
        def inbound(i,j):
            return 0<=i<len(mat) and 0<=j<len(mat[0])
        directions=[(0,1),(1,0),(0,-1),(-1,0)]

        rows=len(mat)
        cols=len(mat[0])

        q=deque()



        for i in range(rows):
            for j in range(cols):

                if mat[i][j]==1:
                    q.append((i,j))
        result=[[0]*cols for _ in range(rows)]

        while q:
            r,c=q.popleft()

            for dr,dc in directions:
                nr=r+dr
                nc=c+dc

                if inbound(nr,nc) and mat[nr][nc]!=1:
                    result[nr][nc]=result[r][c]+1
                    mat[nr][nc]=1
                    q.append((nr,nc))
        return result

        