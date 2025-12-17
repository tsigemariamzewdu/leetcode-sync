class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        sl=list(s)
        for i in range(1,n-1):
            for j in range(n-i):
                d1 = ord(sl[j])-ord("0")
                d2 = ord(sl[j + 1])-ord("0")
                sl[j] = chr(((d1 + d2) % 10) + ord("0"))
        return sl[0] == sl[1]