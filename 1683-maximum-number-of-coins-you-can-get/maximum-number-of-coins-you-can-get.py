class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n=len(piles)
        div=n//3
        piles=piles[div:]
        summ=0
        for i in range(len(piles)):
            if i%2==0:
                summ+=piles[i]
        return summ

        