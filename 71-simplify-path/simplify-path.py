class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack=[]
        current=""

        for c in path +"/":
            if c=="/":
                if current == "..":
                    if stack:
                        stack.pop()
                elif current != "" and current !=".":
                    stack.append(current)
                current="" # reseting the current 
            

            else:
                current += c
        return "/"+"/".join(stack) # to change the stack to string by putting the slash in between 
        
                
           