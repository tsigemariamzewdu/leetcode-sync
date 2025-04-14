class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 
        directions=[(1,0),(0,1),(0,-1),(-1,0)]
        visited= [[False for i in range(len(board[0]))] for j in range(len(board))]
        
        def isedge(i,j):
            return i==0 or i==len(board)-1 or j==0 or j==len(board[0])-1

        def dfs(i,j):
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!="O":
                return
            board[i][j]="E"
           

            for dr,dc in directions:
                nr=i+dr
                nc=j+dc
                dfs(nr,nc)



        for i in range(len(board)):
            for j in range(len(board[0])):
                if  board[i][j]=='O' and  isedge(i,j):
                    dfs(i,j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="O":
                    board[i][j]="X"


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="E":
                    board[i][j]="O"
        