class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        nums.sort()
        mydict = {}
        for i in nums:
            if i in mydict:
                mydict[i] += 1
            else:
                mydict[i] = 1
        
        left = 0
        right = 1
        maxnum = 0
        
        while right < len(nums): 
            if nums[right] - nums[left] == 1:  
                total = mydict[nums[left]] + mydict[nums[right]]  
                maxnum = max(maxnum, total)
                left += 1
                right += 1
            elif nums[right] - nums[left] > 1:  
                left += 1
            else:  
                right += 1
        
        return maxnum
