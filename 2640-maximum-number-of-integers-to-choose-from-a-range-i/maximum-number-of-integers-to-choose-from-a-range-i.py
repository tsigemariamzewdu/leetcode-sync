class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
    

        eligible = [i for i in range(1, n + 1) if i not in banned_set]
    
    
        eligible.sort()
    
   
        total_sum = 0
        count = 0
    
   
        for num in eligible:
            if total_sum + num > maxSum:
                break
            total_sum += num
            count += 1
        
        return count