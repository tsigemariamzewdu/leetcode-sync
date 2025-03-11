class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        def helper(n):
            if n==1:
                return True
            if n%4!=0 or n==0:
                return False
            return helper(n/4)
        return helper(n)

            

      