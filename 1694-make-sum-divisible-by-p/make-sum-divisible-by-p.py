class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if sum(nums)%p==0:
            return 0
        rem=sum(nums)%p
        # print(rem)
        mini=float("inf")
        cursum=0

        mapp={0: -1}
        for i , n in enumerate(nums):
            cursum=(cursum+n)%p
            prefix=(cursum- rem +p)%p
            if  prefix in mapp:
                l=i-mapp[prefix]
                mini=min(mini,l)
            mapp[cursum]=i


        return mini if mini !=len(nums) else -1


        

       





       

       

        