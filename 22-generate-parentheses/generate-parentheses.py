class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        def isvalid(arr):
            stack=[]
            for i in arr:
                if i=="(":
                    stack.append(i)
                else:
                    if stack:
                        stack.pop()
                    else:
                        return False
            if stack:
                return False
            return True

        path=[]
        ans=[]
        def backtrack(idx):

            if idx>=n*2:
                ans.append("".join(path[:]))
                return

            for i in "()":
                path.append(i)
                backtrack(idx+1)
                path.pop()
        backtrack(0)
        result=[]
        for j in ans:
            if isvalid(j):
                result.append(j)
        return result
