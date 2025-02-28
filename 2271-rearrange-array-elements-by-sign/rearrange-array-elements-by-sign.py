class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posarr=[]
        negarr=[]
        for i in nums:
            if i>0:
                posarr.append(i)
            else:
                negarr.append(i)
        i=0
        j=0
        res=[]
        while i<len(posarr) and j<len(negarr):
            res.append(posarr[i])
            res.append(negarr[j])
            i+=1
            j+=1
        return res

        