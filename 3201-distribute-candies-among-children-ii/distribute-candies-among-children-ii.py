class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        total=0
        for i in range(0, min(n,limit)+1):
            minj=max(0,n-i-limit)
            maxj=min(limit,n-i)
            total += max(0,maxj-minj+1)
        return total