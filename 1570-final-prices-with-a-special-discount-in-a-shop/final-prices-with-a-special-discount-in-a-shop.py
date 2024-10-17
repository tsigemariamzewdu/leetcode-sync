class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # okay now i should use stack as far as the goal 
        stack=[]
        result=prices[:] # here we are copying the prices so that i can change if something meets the requirement 
        for i in range(len(prices)):
            while stack and prices[stack[-1]]>=prices[i]:
                index=stack.pop()
                result[index]-=prices[i]
           
                # this is where i got stuck 
            stack.append(i)
        return result
   
        