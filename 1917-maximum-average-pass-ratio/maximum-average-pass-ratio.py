class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        maxheap=[]

        res=0
        for p,n in classes:
            heapq.heappush(maxheap,[(p/n)-((p+1)/(n+1)),p,n])
            res+=p/n
          
        # print(maxheap)
        
        for i in range(extraStudents):
            ratio,x,y=heapq.heappop(maxheap)
            # print(x,y)
            res+=-ratio
            x+=1
            y+=1
            heapq.heappush(maxheap,[(x/y)-((x+1)/(y+1)),x,y])



        return res/len(classes)
        