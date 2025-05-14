class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x=deque(bin(x)[2:])
        y=deque(bin(y)[2:])

        maxi=max(len(y),len(x))

        if len(x)==maxi:
            while len(y)<maxi:
                y.appendleft("0")
        else:
            while len(x)<maxi:
                x.appendleft("0")
        # print(x)
        # print(y)
        count=0
        i=0
        while i<maxi:
            if x[i]!=y[i]:
                count+=1
            i+=1
        return count

        