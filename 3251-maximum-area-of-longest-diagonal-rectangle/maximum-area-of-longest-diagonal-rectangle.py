class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        res,diag=0,0
        for length,width in dimensions:
            newdiag=math.sqrt(length**2 + width **2)
            area=length*width
        
            if newdiag>diag:
                diag=newdiag
                res=area
            elif newdiag==diag:
                res=max(res,area)
                
      
        return res
        