class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[[".",0]]

        for i in s:
            if stack[-1][0]==i:
                stack[-1][1]+=1

                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append([i,1])
        res=[]
        for letter,count in stack:
            res.append(letter*count)
        return "".join(res)


       


        