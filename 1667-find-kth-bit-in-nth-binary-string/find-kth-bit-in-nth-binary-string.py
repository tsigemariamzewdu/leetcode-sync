class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def find(n):
            if n==1:
                return "0"
            else:
                prev=find(n-1)
                inverted=[]
                for i in prev:
                    if i=="0":
                        inverted.append("1")
                    else:
                        inverted.append("0")
                inverted="".join(inverted)

                result=prev + "1"+ "".join(reversed(inverted))
            return result
        return (find(n)[k-1])