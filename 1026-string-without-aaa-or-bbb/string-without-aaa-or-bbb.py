class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res=[]
        if b>a:
            while b>0 or a>0:
                if b>=2 and b>a:
                    res.append("b")
                    res.append("b")
                    b-=2
                else:
                    if b:
                        res.append("b")
                        b-=1 
               
                if a:
                    res.append("a")
                    a-=1
        elif a>b:
            while b>0 or a>0:
                if a>=2 and a>b:
                    res.append("a")
                    res.append("a")
                    a-=2
                else:
                    if a:
                        res.append("a")
                        a-=1
                
                
                if b:
                    res.append("b")
                    b-=1
        else:
            while b>0 or a>0:
                res.append("a")
                a-=1
                res.append("b")
                b-=1
                

        return "".join(res)
                
