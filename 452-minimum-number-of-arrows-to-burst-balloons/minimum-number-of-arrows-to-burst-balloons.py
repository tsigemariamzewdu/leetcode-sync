class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        result=len(points)
        
        count=1
        points.sort()
        reach=points[0][1]
        print(points)
       
        
        for i in range(len(points)):
            if points[i][0]<=reach:
                reach=min(reach,points[i][1])
                continue
            else:
                count+=1
                reach=points[i][1]
            # print(reach)
        return count

      

        