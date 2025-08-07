class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1:
            return True
        for i in range(math.isqrt(num) + 1):
            if i*i ==num:
                return True
        return False