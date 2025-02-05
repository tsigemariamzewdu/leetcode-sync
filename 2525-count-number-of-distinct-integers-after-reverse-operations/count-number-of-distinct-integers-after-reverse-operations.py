class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        newset=set()
        for i in nums:
            newset.add(i)
            newset.add(int(str(i).rstrip()[::-1]))
        return len(newset)



        