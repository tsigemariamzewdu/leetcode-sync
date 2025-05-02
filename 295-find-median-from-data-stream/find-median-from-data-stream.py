class MedianFinder:

    def __init__(self):
        self.maxheap=[]
        self.minheap=[]
        

    def addNum(self, num: int) -> None:
        if not self.maxheap or num<=-self.maxheap[0]:
            heappush(self.maxheap,-num)
        else:
            heappush(self.minheap,num)
        

        if len(self.maxheap)>len(self.minheap)+1:
            pope=-heappop(self.maxheap)
            heappush(self.minheap,pope)
        elif len(self.minheap)>len(self.maxheap):
            pope=heappop(self.minheap)
            heappush(self.maxheap,-pope)
        

        

    def findMedian(self) -> float:
        if len(self.minheap)==len(self.maxheap):
            return (self.minheap[0]- self.maxheap[0])/2
        return -self.maxheap[0]
       
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()