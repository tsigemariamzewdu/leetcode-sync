class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>0:
            num= str(x)
            num=num[::-1]

            newnum=''
            for i in range(len(num)):
                if num[0]==0:
                    continue
                else:
                    newnum+=num[i]
            number=int(newnum)
        else:
            x=-1*x
            num= str(x)
            num=num[::-1]

            newnum=''
            for i in range(len(num)):
                if num[0]==0:
                    continue
                else:
                    newnum+=num[i]
            number= -1* int(newnum)
        if -(2**31) < number <2**31:
            return number
        else:
            return 0
        