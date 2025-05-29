class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        lists=[]
        for i in s:
            lists.append(ord(i)-96)
        for i in t:
            lists.append(ord(i)-96)
        res=0
        for i in lists:
            res ^= i
        return chr(res+96)


        




