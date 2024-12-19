class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        largestNumberOfChunk = 0
        current_max = 0
        
        for i in range(len(arr)):
            current_max = max(current_max, arr[i])
            
            if current_max == i:
                largestNumberOfChunk += 1
        
        return largestNumberOfChunk
