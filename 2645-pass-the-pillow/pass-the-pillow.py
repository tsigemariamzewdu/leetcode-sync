class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i=1
        direction =1 if time>0 else -1
        t=1
        while t<=time:
            i+=direction
            if i==n or i==1:
                direction*=-1
            t+=1
        return i






        