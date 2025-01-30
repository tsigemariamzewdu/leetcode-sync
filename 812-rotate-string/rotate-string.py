class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        count=0
        while count<len(s):
            s=s[1:]+s[0]
            count+=1
            if s==goal:

                return True
        return False


        