class Solution:
    def canCross(self, stones: List[int]) -> bool:
        memo={}
        stone_set=set(stones)
        if stones[0]!=0 or stones[1]!=1:
            return False

        def dp(i,k):
            if i==stones[-1]:
                return True
            state=(i,k)

            if state not in memo:
                
                for j in [k-1,k,k+1]:
                    if j >0 and (i+j) in stone_set:
                        if dp(i+j,j):
                            memo[state]=True
                            return True
                
                memo[state]=False
            return memo[state]
        return dp(0,0)
            
            
        