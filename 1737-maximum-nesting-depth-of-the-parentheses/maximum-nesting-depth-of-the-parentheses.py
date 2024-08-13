class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        # lets declare an empty stack
        stack=[]
        maxnested=0
        for i in s:
            if i =="(":
                stack.append(i)
            elif i ==")":
                maxnested=max(maxnested,len(stack))
                stack.pop()
        return maxnested
        