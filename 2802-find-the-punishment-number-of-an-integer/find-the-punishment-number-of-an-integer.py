class Solution:
    def punishmentNumber(self, n: int) -> int:


        def helper(number):
            ans=[]

            path=[]
            def backtrack(idx):
                nonlocal path
               

                if idx>=len(number):
              
                    if sum(path)==int(int(number)**(1/2)):
                        ans.append(int(number))
                        return 
                if idx>len(number):
                    return 
          
                for i in range(idx,len(number)):
                    if ans:
                        return
                    val=int(number[idx:i+1])
                    path.append(val)
                    
                    backtrack(i+1)
                    path.pop()
            backtrack(0)
            if ans:
                return ans[0]
            else:
                return 0
               
           
        ans=[1]
     
        for i in range(9,n+1):
            number=i**2
          
            toadd=helper(str(number))
            ans.append(toadd)
            
        return sum(ans)
            
