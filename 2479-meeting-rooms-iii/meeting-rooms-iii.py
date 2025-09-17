class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free=[i for i in range(n)]
        used=[]

        count=[0]*n
        for start,end in meetings:

            while used and start>=used[0][0]:
                e,room=heapq.heappop(used)
                heapq.heappush(free,room)

            if not free:
                ee,room=heapq.heappop(used)
                end=ee+(end-start)
                heapq.heappush(free,room)

            room=heapq.heappop(free)
            heapq.heappush(used,(end,room))
            count[room]+=1




        return count.index(max(count))

        