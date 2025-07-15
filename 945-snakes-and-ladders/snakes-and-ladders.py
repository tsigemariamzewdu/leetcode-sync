class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n=len(board)
        mapp={}
        num=1

        right=(n-1)%2

        for row in range(n-1,-1,-1):
            if row%2==right:
                cols=list(range(n))
            else:
                cols=list(range(n-1,-1,-1))
            for col in cols:
                mapp[num]=(row,col)
                num+=1
        
        q=deque()
        q.append([1,0])

        visited=set()

        while q:
            number,moves=q.popleft()
            for i in range(1,7):
                nextnum=number + i
                r,c=mapp[nextnum]
                if board[r][c]!=-1:
                    nextnum=board[r][c]
                if nextnum == n*n:
                    return moves+1
                if nextnum not in visited:
                    visited.add(nextnum)
                    q.append([nextnum,moves+1])
        return -1
        