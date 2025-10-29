class Solution:
    def smallestNumber(self, n: int) -> int:
        nn=bin(n)
        return( 2 **len(nn[2:]) -1)
        