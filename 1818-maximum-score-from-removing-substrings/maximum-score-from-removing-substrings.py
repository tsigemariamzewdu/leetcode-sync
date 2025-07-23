class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x >= y:
            res = 0
            stack = []
         
            for i in s:
                if i == 'b':
                    if stack and stack[-1] == 'a':
                        stack.pop()
                        res += x
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
            
            newstack = []
            for i in stack:
                if i == 'a':
                    if newstack and newstack[-1] == 'b':
                        newstack.pop()
                        res += y
                    else:
                        newstack.append(i)
                else:
                    newstack.append(i)
            return res
        else:
            res = 0
            stack = []
          
            for i in s:
                if i == 'a':
                    if stack and stack[-1] == 'b':
                        stack.pop()
                        res += y
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
            
            newstack = []
            for i in stack:
                if i == 'b':
                    if newstack and newstack[-1] == 'a':
                        newstack.pop()
                        res += x
                    else:
                        newstack.append(i)
                else:
                    newstack.append(i)
            return res