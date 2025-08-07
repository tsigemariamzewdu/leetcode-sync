class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1:
            return True
        high=math.isqrt(num)+1
        low=1

        while low<=high:
            mid=(low+high)//2
            if mid*mid==num:
                return True
            elif mid*mid<num:
                low=mid+1
            else:
                high=mid-1
        return False
       