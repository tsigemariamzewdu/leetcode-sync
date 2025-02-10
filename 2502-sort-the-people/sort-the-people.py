class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heighttonames={}
        result=[]
        for ii in range(len(heights)):
            heighttonames[heights[ii]]=names[ii]
        n=len(heights)
        for i in range(n):
            is_sorted=True
            for j in range(1,n-i):
                if heights[j]<heights[j-1]:
                    heights[j],heights[j-1]=heights[j-1],heights[j]
                    is_sorted=False
            if is_sorted:
                break
        for k in range(n-1,-1,-1):
            result.append(heighttonames[heights[k]])
        return result

        