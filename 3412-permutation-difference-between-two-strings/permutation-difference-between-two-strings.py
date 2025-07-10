class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        dicts={}
        dictt={}

        for i,l in enumerate(s):
            dicts[l]=i
        for i,le in enumerate(t):
            dictt[le]=i
        # print(dicts,dictt)
        ans=0

        for i in range(len(s)):
            ans += abs(dicts[s[i]]-dictt[s[i]])
        return ans


        