class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n=len(points)
        count=0

        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                x1,y1=points[i]
                x2,y2=points[j]

                if x1<=x2 and y1>=y2:
                    valid=True
                    minx,maxx=min(x1,x2),max(x1,x2)
                    miny,maxy=min(y1,y2),max(y1,y2)

                    for k in range(n):
                        if k==i or k==j:
                            continue
                        x3,y3=points[k]
                        if minx<=x3<=maxx and miny<=y3<=maxy:
                            valid=False
                            break
                    if valid:
                        count+=1
        return count