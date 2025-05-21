class Solution:
    def reverseWords(self, s: str) -> str:
        res=s.split()
        res=reversed(res)
        return " ".join(res)
        