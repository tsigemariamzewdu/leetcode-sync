from collections import Counter
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        arr=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                arr.append(nums[i]*nums[j])
        
        counter=Counter(arr)
        

        count=0
        for i in counter:
            if counter[i]>1:
                count+=(counter[i]*(counter[i]-1))//2
        return count*8
        
        

          





            