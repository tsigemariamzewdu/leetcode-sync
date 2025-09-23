class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo={}
        def dp(i,j):
            if i==len(text1) or j==len(text2):
                return 0
            state=(i,j)
            if state not in memo:
            
                if text1[i]==text2[j]:
                    memo[state]= 1 + dp(i+1,j+1)
                else:
                    memo[state]= max(dp(i+1,j),dp(i,j+1))
            return memo[state]
        return dp(0,0)