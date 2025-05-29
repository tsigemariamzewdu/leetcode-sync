class Solution:
    def addDigits(self, num: int) -> int:
        lists=list(str(num))

        while len(lists)!=1:
           summ=0
           for i in lists:
            summ += int(i)
            lists=list(str(summ))
        return int(lists[0])
       

        