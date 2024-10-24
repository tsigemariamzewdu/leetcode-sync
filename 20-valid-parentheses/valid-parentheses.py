class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in '({[':
                stack.append(i)
            elif  stack and i=="]" and stack[-1]=="[":
                stack.pop()
            elif stack and  i=="}" and stack[-1]=="{":
                stack.pop()
            elif stack and  i==")" and stack[-1]=="(":
                stack.pop()
            else:
                stack.append(i)
        return len(stack)==0

        