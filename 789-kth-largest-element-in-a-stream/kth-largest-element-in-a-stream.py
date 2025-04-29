class KthLargest:
    def parent(self,j):
        return (j-1)//2
    def heappush(self,heap,value):
        heap.append(value)
        current=len(heap)-1
        heapify_up(heap,current)
    def heapify_up(self,heap,j):
        p=parent(j)
        if j>0 and heap[j]<heap[p]:
            self.swap(heap,j,p)
            self.heapify_up(heap,p)
    def swap(self, heap, i, j):
        heap[i], heap[j] = heap[j], heap[i] 

    def heapify_down(self, heap, n, current_idx):
        small_child_idx = current_idx
        left_idx = 2 * current_idx + 1
        right_idx = 2 * current_idx + 2
        if left_idx < n and heap[left_idx] < heap[small_child_idx]:
            small_child_idx = left_idx 
        if right_idx < n and heap[right_idx] < heap[small_child_idx]:
            small_child_idx = right_idx
        if small_child_idx != current_idx:
            self.swap(heap, current_idx, small_child_idx)
            self.heapify_down(heap, n, small_child_idx)

    def heapify(self, array):
        n = len(array)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(array, n, i)

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        nums.sort(reverse=True)

        self.min_heap=nums[:k]
        self.heapify(self.min_heap)

        for num in nums[k:]:
            self.add(num)
      

        

    def add(self, val: int) -> int:
        if len(self.min_heap)<self.k:
            self.min_heap.append(val)
            self.heapify(self.min_heap)
        elif val>self.min_heap[0]:
            self.min_heap[0]=val
            self.heapify_down(self.min_heap,len(self.min_heap),0)
        
        return self.min_heap[0]

        
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)