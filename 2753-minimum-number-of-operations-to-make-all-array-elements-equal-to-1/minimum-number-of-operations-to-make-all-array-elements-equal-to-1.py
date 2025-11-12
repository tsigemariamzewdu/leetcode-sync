class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if 1 in nums:
            return len(nums)-nums.count(1)
        mini= float('inf')
        for right in range(len(nums)):
            cur_gcd= nums[right]
            for left in range(right,-1,-1):
                cur_gcd= math.gcd(cur_gcd,nums[left])
                if cur_gcd==1:
                    mini=min(mini,right-left+1)
        if mini==float('inf'):
            return -1
        return len(nums) + mini-2
