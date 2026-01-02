class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n=len(nums)//2
        counter=Counter(nums)
        for i in counter:
            if counter[i]==n:
                return i
                
        