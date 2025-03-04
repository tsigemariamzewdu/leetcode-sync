class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
       
        count=0
       
        while maxDoubles and target>=1:
            if target%2==0:
                count+=1
                maxDoubles-=1
                print(target)
                
                target=target//2
                
            else:
                count+=1
                target-=1

            
        return count+target-1



