class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for i in stones:
            heappush(heap,-i)
        while len(heap)>1:
            first=-heappop(heap)
            second=-heappop(heap)
            if first==second:
                continue
            else:
                heappush(heap,-(abs(second-first)))
        if heap:
            return -heap[0]
        return 0

        