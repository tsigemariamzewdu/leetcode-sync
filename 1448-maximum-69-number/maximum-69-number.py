class Solution:
    def maximum69Number (self, num: int) -> int:
        strnum=str(num)
        listnum=[]
        for i in strnum:
            listnum.append(i)
        for i in range(len(listnum)):
            if listnum[i]=="6":
                listnum[i]="9"
                break
        return int( "".join(listnum))