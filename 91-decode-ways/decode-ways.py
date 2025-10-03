class Solution:
    def numDecodings(self, s: str) -> int:
        memo={}
       
        def dp(word):
            if not word:
                return 1
            if word[0]=="0":
                return 0
            
            if word not in memo:
                memo[word]=dp(word[1:])
                if len(word)>=2 and int(word[:2])<=26:
                    memo[word]+=dp(word[2:])
                    
            return memo[word]
        return dp(s)
        