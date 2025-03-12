class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        result=[]
        for i in range(1,n+1):
            result.append(i)
        si=0
        while len(result)>1:
            ri=(si+k-1)%len(result)
            result.pop(ri)
            si=ri

        return result[0]
            