class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        def helper(current,limit,result):
            if current >limit:
                return
            
            result.append(current)

            for i in range(10):
                next=current*10 + i

                if next<=limit:
                    helper(next,limit,result)
                else:
                    break
        result=[]
        for i in range(1,10):
            helper(i,n,result)
        return result