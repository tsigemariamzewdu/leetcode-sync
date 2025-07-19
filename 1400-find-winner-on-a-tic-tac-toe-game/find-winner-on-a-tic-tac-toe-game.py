class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid=[]
        for i in range(3):
            grid.append([0,0,0])
        for i in range(len(moves)):
            x,y=moves[i]
            if i%2==0:
                grid[x][y]="X"
            else:
                grid[x][y]="O"
        diag=[]
        anti=[]
        for i in range(3):
            for j in range(3):
                if i==j:
                    diag.append(grid[i][j])
                if i+j==2:
                    anti.append(grid[i][j])
        if len(diag)==3:
            df=diag[0]
            dffound=True
            for i in range(1,3):
                if diag[i]!=df:
                    dffound=False
                    break
            if dffound:
                if df=="X":
                    return "A"
                elif df=="O":
                    return "B"
        if len(anti)==3:
            af=anti[0]
            afound=True
            for i in range(1,3):
                if anti[i]!=af:
                    afound=False
                    break
            if afound:
                if af=="X":
                    return "A"
                elif af=="O":
                    return "B"


        for i in range(3):
            row=grid[i]
            first=row[0]
            found =True
            for k in range(1,3):
                if row[k]!=first:
                    found=False
                    break
            if found:
                if first=="X":
                    return "A"
                elif first=="O":
                    return "B"
        for i in range(3):
            firstcol=[]
            for j in range(3):
                firstcol.append(grid[j][i])
            fc=firstcol[0]
            colfound=True
            for l in range(1,3):
                if firstcol[l]!=fc:
                    colfound=False
            if colfound:
                if fc=="X":
                    return "A"
                elif fc=="O":
                    return "B"
        if len(moves)==9:
            return "Draw"
        return "Pending"



        