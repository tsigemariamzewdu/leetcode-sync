class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        result=[0]*len(heights)
        stack=[]

        for i in range(len(heights)-1,-1,-1):
            while stack and heights[i]>stack[-1]:
                stack.pop()
                result[i]+=1
            if stack:
                result[i]+=1

                
            stack.append(heights[i])
        return result

        