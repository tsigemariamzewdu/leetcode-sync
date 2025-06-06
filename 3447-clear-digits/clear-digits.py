class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for i in s:
            if not i.isdigit():
                stack.append(i)
            else:
                stack.pop()
        return "".join(stack)
        