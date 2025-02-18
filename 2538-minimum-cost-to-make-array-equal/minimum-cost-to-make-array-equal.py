class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        
        merged = sorted(zip(nums, cost))
        n = len(merged)
        pref_cumulative = [0]*(n + 1)
        suf_cumulative = [0]*(n + 1)
        
        tot_c = 0
        for i, (num, c) in enumerate(merged):
            diff = (num - merged[i - 1][0] if i > 0 else 0) 
            cur_cost = diff*tot_c
            pref_cumulative[i] += pref_cumulative[i - 1] + cur_cost 
            tot_c += c
        
        tot_c = 0
        for i in range(n - 1, -1, -1):
            num, c = merged[i]
            diff = (merged[i + 1][0] - num if i + 1 < n else 0)
            cur_cost = diff*tot_c
            suf_cumulative[i] += suf_cumulative[i + 1] + cur_cost 
            tot_c += c
        
        ans = float('inf')
        for i in range(n):
            ans = min(ans, pref_cumulative[i] + suf_cumulative[i])
        
        return ans