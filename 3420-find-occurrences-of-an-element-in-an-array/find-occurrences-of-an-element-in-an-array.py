class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        mapp=defaultdict(list)

        for i in range(len(nums)):
            mapp[nums[i]].append(i)
        print(mapp)
        ans=[]
        flag=False
        for i in mapp:
            if i==x:
                flag=True
                for j in queries:
                    if len(mapp[i])>j-1:
                        ans.append(mapp[i][j-1])
                    else:
                        ans.append(-1)
        if not flag:
            return [-1]*len(queries)
        return ans

                   
        