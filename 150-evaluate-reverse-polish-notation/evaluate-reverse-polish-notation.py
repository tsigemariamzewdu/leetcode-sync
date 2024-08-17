class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        for i in tokens:
            if i in "+-*/":
                num2=stack.pop()
                num1=stack.pop()
                if i =="+":
                    stack.append(num1+num2)
                if i =="-":
                    stack.append(num1-num2)
                if i =="*":
                    stack.append(num1*num2)
                if i =="/":
                    if num1*num2 <0 and num1%num2 !=0:
                        stack.append((num1//num2) +1)
                    else:
                        stack.append(num1//num2)
                    
            else:
                stack.append(int(i))
        return stack[0]
        