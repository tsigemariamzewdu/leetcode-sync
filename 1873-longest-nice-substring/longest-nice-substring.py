class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        _set=set(s)

        for i in range(len(s)):
            if len(s)<=1:
                return ""
            ch=s[i]
            if ch.swapcase()  not in _set:
                left=self.longestNiceSubstring(s[:i])
                right=self.longestNiceSubstring(s[i+1:])

                if len(right)>len(left):
                    return right
                return left
        return s

        