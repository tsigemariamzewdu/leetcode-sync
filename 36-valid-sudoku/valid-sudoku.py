from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # column check
        for col in board:
            counter=Counter(col)
            for i in counter:
                if i!="." and counter[i]>1:
                    return False
        # row check
        for c in range(len(board[0])):
            result=[]
            for r in range(len(board)):
                result.append(board[r][c])
            cr=Counter(result)
            for j in cr:
                if j!="." and cr[j]>1:
                    return False
        # 3 x 3 check
        # for i in range(9):
        #     count=0
        res1=[]
        for r in range(3):
            for c in range(3):
                res1.append(board[r][c])
        countres1=Counter(res1)
        for k in countres1:
            if countres1[k]>1 and k!=".":
                return False
        
        res2=[]
        for r in range(3):
            for c in range(3,6):
                res2.append(board[r][c])
        countres2=Counter(res2)
        for k in countres2:
            if countres2[k]>1 and k!=".":
                return False
        res3=[]
        for r in range(3):
            for c in range(6,9):
                res3.append(board[r][c])
        countres3=Counter(res3)
        for k in countres3:
            if countres3[k]>1 and k!=".":
                return False

        res4=[]
        for r in range(3,6):
            for c in range(3):
                res4.append(board[r][c])
        countres4=Counter(res4)
        for k in countres4:
            if countres4[k]>1 and k!=".":
                return False
        res5=[]
        for r in range(3,6):
            for c in range(3,6):
                res5.append(board[r][c])
        countres5=Counter(res5)
        for k in countres5:
            if countres5[k]>1 and k!=".":
                return False
        res6=[]
        for r in range(3,6):
            for c in range(6,9):
                res6.append(board[r][c])
        countres6=Counter(res6)
        for k in countres6:
            if countres6[k]>1 and k!=".":
                return False

        res7=[]
        for r in range(6,9):
            for c in range(3):
                res7.append(board[r][c])
        countres7=Counter(res7)
        for k in countres7:
            if countres7[k]>1 and k!=".":
                return False
        print(res7)
        res8=[]
        for r in range(6,9):
            for c in range(3,6):
                res8.append(board[r][c])
        countres8=Counter(res8)
        for k in countres8:
            if countres8[k]>1 and k!=".":
                return False
        print(res8)
        res9=[]
        for r in range(6,9):
            for c in range(6,9):
                res9.append(board[r][c])
        countres9=Counter(res9)
        for k in countres9:
            if countres9[k]>1 and k!=".":
                return False

        
        

        return True



        