class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        count=0
        costs.sort()
        if costs[0]>coins:
            return 0
        for i in costs:
            coins-=i
            if coins>=0:
                count+=1
            
            if coins<0:
                break
            
        return count

       