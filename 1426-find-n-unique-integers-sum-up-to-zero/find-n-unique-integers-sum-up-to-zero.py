class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[]
        if n%2==0:
            for i in range(-(n//2),(n//2)+1):
                if i==0:
                    continue
                res.append(i)
            return res
        else:
            for i in range(-(n//2),(n//2)+1):
                res.append(i)
           
            return res

        