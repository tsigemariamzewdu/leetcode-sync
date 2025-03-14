class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def helper(n):
            if n==1:
                return True
            if n%3!=0 or n==0:
                return False
            else:
                return helper(n//3)
        return helper(n)
            