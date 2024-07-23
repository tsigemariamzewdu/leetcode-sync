class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[]
        l,r=0,len(numbers)-1
        while l<r:
            sum2= numbers[l]+numbers[r]
            if sum2>target:
                r-=1
            if sum2< target:
                l +=1
            if sum2== target:
                res.append(l+1)
                res.append(r+1)
                l+=1
                r-=1
        return res
        