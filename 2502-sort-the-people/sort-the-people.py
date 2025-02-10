class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heighttonames={}
        result=[]
        for ii in range(len(heights)):
            heighttonames[heights[ii]]=names[ii]
        n=len(heights)
        for i in range(1,n):
            while heights[i]<heights[i-1]:
                heights[i],heights[i-1]=heights[i-1],heights[i]
                if i ==1 or i ==n:
                    continue
            
                i-=1



        for k in range(n-1,-1,-1):
            result.append(heighttonames[heights[k]])
        return result

        