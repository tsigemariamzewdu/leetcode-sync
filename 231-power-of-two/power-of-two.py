class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0:
            return False
        num=bin(n).count("1")
        return num==1
            
