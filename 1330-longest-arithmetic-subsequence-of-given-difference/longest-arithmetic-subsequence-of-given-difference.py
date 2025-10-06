class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp=defaultdict(int)
        maxi=0

        for n in arr:
            dp[n]=dp[n-difference]+1
            maxi=max(maxi,dp[n])
        return maxi
