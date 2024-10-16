class Solution(object):
    def calPoints(self, ops):
        """
        :type operations: List[str]
        :rtype: int
        """
        # this looks clear let me try it
        stack=[]
        for i in range(len(ops)):
            if ops[i].lstrip('-').isdigit():
                stack.append(int(ops[i]))
            elif ops[i]=="C" and stack:
                stack.pop()
            elif ops[i]=="D" and stack:
                newentry=stack[-1]*2
                stack.append(newentry)
            elif ops[i]=="+" and stack:
                newentry= stack[-1]+ stack[-2]
                stack.append(newentry)
        return sum(stack)


        