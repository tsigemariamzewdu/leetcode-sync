class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        
        for char in expression:
            if char == ')':
                temp = []
                
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                
                stack.pop()  
                operator = stack.pop()  
                
                if operator == '|':
                    stack.append('t' if 't' in temp else 'f')  
                
                elif operator == '&':
                    stack.append('f' if 'f' in temp else 't')  
                
                elif operator == '!':
                    stack.append('f' if temp[0] == 't' else 't')  
                
            elif char != ',':
                stack.append(char)  
        
        return stack.pop() == 't' 
