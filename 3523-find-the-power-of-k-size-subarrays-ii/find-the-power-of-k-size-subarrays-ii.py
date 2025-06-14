class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        current=0
        for i in range(len(nums)):
            if i==0 or nums[i]==nums[i-1]+1:
                current+=1
            else:
                current =1
            if i+1 >= k:
                if current>=k:
                    ans.append(nums[i])
                else:
                    ans.append(-1)
        return ans        