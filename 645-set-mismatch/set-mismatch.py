class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counter=Counter(nums)
        res=[]
        for i in counter:
            if counter[i]==2:
                res.append(i)
        setn=set(nums)
        for j in range(1,len(nums)+1):
            if j not in setn:
                res.append(j)
        return res
            





        