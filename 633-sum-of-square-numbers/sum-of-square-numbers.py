class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        cand=[]
        for i in range(0,int(c**(0.5))+1):
            cand.append(i)
        l=0
        r=len(cand)-1
        print(cand)
        while l<=r:
            if cand[l]**2 + cand[r]**2==c:
                return True
            elif  cand[l]**2 + cand[r]**2<c:
                l+=1
            elif  cand[l]**2 + cand[r]**2>c:
                r-=1
           
        return False
        