class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times=[(t[0],t[1],i) for i,t  in enumerate(times)]
        times.sort()

        usedchair=[]
        avachair=[i for i in range(len(times))]

        for a,l,i in times:

            while usedchair and usedchair[0][0]<= a:
                le,chair=heapq.heappop(usedchair)
                heapq.heappush(avachair,chair)
            chair=heapq.heappop(avachair)
            heapq.heappush(usedchair,(l,chair))

            if i==targetFriend:
                return chair
