class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen={}

        while n != 1:
            if n in seen:
                return False
            seen[n]=True

            nxt=0
            while n>0:
                digit=n%10
                nxt += digit**2
                n //=10
            n=nxt
        return True

