class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        myset=set()
        for i in nums:
            myset.add(i)
        lists=list(myset)
        lists.sort(reverse=True)
        if len(lists)>=3:
            return lists[2]
        return max(lists)

        