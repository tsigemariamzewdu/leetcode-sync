class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ans=float("-inf")
        for i in range(len(points)-2):
            for j in range(i+1,len(points)-1):
                for k in range(j+1,len(points)):
                    p1=points[i]
                    p2=points[j]
                    p3=points[k]
                    
                    ans=max(ans,0.5*(abs(p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1])+p3[0]*(p1[1]-p2[1]))))
        return ans