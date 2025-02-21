class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        n=len(beans)
        summ=0

        beans.sort()

        maxarea=0

        for i in range(n):
            summ+= beans[i]
            maxarea=max(maxarea,beans[i]*(n-i))
        return summ-maxarea
        
       

        