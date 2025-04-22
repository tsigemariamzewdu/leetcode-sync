class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        directions=[(0,-1),(-1,0),(0,1),(1,0),(-1,-1),(1,1),(1,-1),(-1,1)]
        rows=len(board)
        cols=len(board[0])
        visited = [[False for i in range(cols)] for j in range(rows)]


        if board[click[0]][click[1]]=="M":
            board[click[0]][click[1]]="X"
            return board

        def inbound(i,j):
            return 0<=i<rows and 0<=j<cols


        def dfs(i,j):
            visited[i][j]=True
            if board[i][j]=="M":
                board[i][j]="X"
                return 
               
            elif board[i][j]=="E":

                count=0
                
                for dr,dc in directions:
                    nr=i+dr
                    nc=j+dc
                    if inbound(nr,nc) and board[nr][nc]=="M":
                        count+=1
                if count==0:
                    board[i][j]="B"

                    for dr,dc in directions:
                        nr=i+dr
                        nc=j+dc
                        if inbound(nr,nc) and not visited[nr][nc]:
                            dfs(nr,nc)
                else:
                    board[i][j]=str(count)
            return board
        return dfs(click[0],click[1])

                   
              
          
            





        