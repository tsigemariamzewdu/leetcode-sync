class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(1,n):
            flag=True
            num1=str(i)
            num2=str(n-i)

            for j in num1:
                if j=="0":
                    flag=False
            for k in num2:
                if k=="0":
                    flag=False
            if flag:
                return [i,n-i]

            
       
        