class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]

        path=[]
        def backtrack(idx):
            if len(path)>=4:
                res.append(".".join(path))
                return
            if idx>len(s)-1:
                return




            if int(s[idx])==0:
                path.append(s[idx])
                backtrack(idx+1)
                path.pop()
            elif 1 <= int(s[idx])<=2:
                for i in range(3):
                    if len(s)>=idx+i+1:
                        val=s[idx:idx+i+1]
                        path.append(val)
                        backtrack(idx+i+1)
                        path.pop()
            else:
                for i in range(2):
                    if len(s)>=idx+i+1:
                        val=s[idx:idx+i+1]
                        path.append(val)
                        backtrack(idx+i+1)
                        path.pop()
        backtrack(0)
        result=[]
        for i in res:
            if len(i) - 3 == len(s):

                result.append(i)
        print(result)
        realresult=[]
        for j in result:
            flag = True
            for k in j.split("."):
                if int(k) > 255:
                    flag = False
            if  flag:
                realresult.append(j)
        return realresult
                    
               
            
           
            


            





        
        















        