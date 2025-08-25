class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans=[]
        for i in range(len(arr)+k):
            if i+1 not in arr:
                ans.append(i+1)
        if len(ans)>k:
            return ans[k-1]
        else:
            return ans[-1]+(k-len(ans))


        