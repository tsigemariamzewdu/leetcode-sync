class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]

        for i in logs:
            if i=="../" and stack:
                stack.pop()
            elif i=="./":
                continue
            elif i!="../" and i!="./":
                stack.append(i)
        return len(stack)