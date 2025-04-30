class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        difflist=[]
        
        for i in range(len(heights)-1):
            first,second=heights[i],heights[i+1]
            diff=second-first
            if diff <=0:
                continue
            else:
                heapq.heappush(difflist,-diff)
                bricks -= diff
               
                if bricks<0:
                    if ladders:
                        ladders-=1
                        bricks += - heapq.heappop(difflist)
                    else:
                        return i
                
        return len(heights)-1



        