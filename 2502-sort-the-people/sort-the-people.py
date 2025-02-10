class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heighttonames={}
        result=[]
        for ii in range(len(heights)):
            heighttonames[heights[ii]]=names[ii]
        n=len(heights)
        for i in range(n):
            for j in range(1,n-i):
                if heights[j]<heights[j-1]:
                    heights[j],heights[j-1]=heights[j-1],heights[j]
        for k in range(n-1,-1,-1):
            result.append(heighttonames[heights[k]])
        return result

        