class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        count=0
        heap=[]

        for  i in piles:
            heapq.heappush(heap,-i)

        res=sum(piles)

        while count<k:
            if heap:
                number=-heapq.heappop(heap)
                res -=number 
                res += ceil(number/2)
                # print(ceil(number/2))
                heapq.heappush(heap,-(ceil(number/2)))
            count +=1
        return res
        

        