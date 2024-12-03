class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum = 0
        prefixsumCount = {0: 1}  
        count = 0
        
        for num in nums:
           
            prefixsum += num
            
            
            if (prefixsum - k) in prefixsumCount:
                count += prefixsumCount[prefixsum - k]  
           
            if prefixsum in prefixsumCount:
                prefixsumCount[prefixsum] += 1 
            else:
                prefixsumCount[prefixsum] = 1  
        
        return count
