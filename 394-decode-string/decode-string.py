class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]

        for i in range(len(s)):
            if s[i] !="]":
                stack.append(s[i])
            else:
                temp=[]
                while stack and stack[-1]!="[":
                    temp.append(stack.pop())
                stack.pop()
                mul=[]
                while stack and stack[-1].isdigit():
                    mul.append(stack.pop())
                temp=temp[::-1]
                mul=mul[::-1]
                
                result=("".join(temp))*int("".join(mul))
                for j in result:
                    stack.append(j)
        return "".join(stack)

       

            
        
        
        


                
