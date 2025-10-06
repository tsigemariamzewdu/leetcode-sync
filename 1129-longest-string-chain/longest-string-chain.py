class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp={}
        maxi=1

        for word in words:
            dp[word]=1
            for i in range(len(word)):
                prev=word[:i]+word[i+1:]
                if prev in dp:
                    dp[word]=max(dp[word],dp[prev]+1)
            maxi=max(maxi,dp[word])
        return maxi