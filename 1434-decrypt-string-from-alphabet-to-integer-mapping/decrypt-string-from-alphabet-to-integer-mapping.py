class Solution:
    def freqAlphabets(self, s: str) -> str:
       
        stack=[]
        ans=[]
        for i in s:
            stack.append(i)
        while stack:
            num=stack.pop()
            if num != "#":
                ans.append(chr(int(num)+96))
            else:
                first=stack.pop()
                second=stack.pop()
                realnum=int(second+first)
                ans.append(chr(realnum+96))
        return "".join(reversed(ans))


        