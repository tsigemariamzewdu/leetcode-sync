class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count =0
        heap=[]
        for i in nums:
            heappush(heap,-i)
        print(heap)
        while heap:
            if count==k-1:
                # print("here")
                ans=-heappop(heap)
                break
            else:
                count +=1
                heappop(heap)

        return ans