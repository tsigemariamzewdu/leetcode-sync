class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        count = 0
        sum1 = 0
        
        for cost in costs:
            if sum1 + cost <= coins:
                sum1 += cost
                count += 1
            else:
                break
        
        return count