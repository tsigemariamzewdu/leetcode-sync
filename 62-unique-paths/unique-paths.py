class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(n-1+m-1,n-1)
        