class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        def pascal(index):
            if index==0:
                return []
            if index==1:
                return [1]
            prev_row=pascal(index-1)
            res_row=[1]*index

            for i in range(1,index-1):
                res_row[i]=prev_row[i]+prev_row[i-1]
            prev_row=res_row
            return prev_row
        return pascal(rowIndex+1)

