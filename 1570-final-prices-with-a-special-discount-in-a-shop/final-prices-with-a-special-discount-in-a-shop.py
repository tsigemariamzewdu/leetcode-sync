class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # i was about to use this one but i think about it and it is not using stack but i dont care as far as it is solving it right cause i am sick today
        n=len(prices)
        result=[]
        for i in range(0,n-1):
            j=i+1
            while j<n-1 and prices[j]>prices[i]:
                j+=1            
            if j==n-1 and prices[j]>prices[i]:
                result.append(prices[i])
            else:
                result.append(prices[i]-prices[j])
        return result+ [prices[n-1]]
   
        