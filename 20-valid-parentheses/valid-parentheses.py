class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack:
                    return False
                top=stack[-1]
                if i ==")" and top=="(":
                    stack.pop()
                    
                elif i =="]" and top=="[":
                    stack.pop()
                    
                elif i =="}" and top=="{":
                    stack.pop()
                else:
                    return False
        return len(stack)==0      