class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        path=[]
        ans=[]

        def backtrack(i):
            # base case
            if i==len(nums):
                ans.append(path[:])
                return
           
                
            backtrack(i+1)
            path.append(nums[i])
            backtrack(i+1)
            path.pop()
                    

        backtrack(0)
        return ans