class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        path=[]
        def backtrack(idx):
            if len(path)==len(nums):
                ans.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] not in path:
           
                    path.append(nums[i])
                    backtrack(idx+1)
                    path.pop()
        backtrack(0)
        return ans



        