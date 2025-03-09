class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        res=0

        for i in s:
            if i=="(":
                stack.append(0)
            else:
                m=stack.pop()
                if m==0:
                    val=1
                else:
                    val=m*2
                if not stack:
                    res+=val
                else:
                    stack[-1]+=val
        return res

        