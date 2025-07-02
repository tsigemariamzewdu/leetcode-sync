class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for i in stones:
            heappush(heap,-i)
        while len(heap)>1:
            fir=-heappop(heap)
            second=-heappop(heap)
            if fir==second:
                continue
            else:
                heappush(heap,-(abs(second-fir)))
        if heap:
            return -heap[0]
        return 0

        