class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # monotonic stack
        result=[0]* len(temperatures) # we intialized with all zeros
        stack=[] # here we have the stack to store the index od the temperatures

        for i , temperature in enumerate(temperatures):# here i am using enumerate since i am concerned about the index
            while stack and temperatures[stack[-1]]<temperature:
                previous=stack.pop()
                result[previous]=i-previous 
            stack.append(i)
        return result



      
                


