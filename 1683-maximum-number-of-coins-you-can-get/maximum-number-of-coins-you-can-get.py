class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort(reverse=True)
        result=0

        n=len(piles)//3 #this tells us how many groups of three are there in the list

        for i in range(n):
            result += piles[2*i +1]
        return result

        