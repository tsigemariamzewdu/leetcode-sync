from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q=deque()
        max_q=deque()

        left=0
        maxsize=0

        for right in range(len(nums)):

            while min_q and min_q[-1] >nums[right]:
                min_q.pop()
            min_q.append(nums[right])


            while max_q and max_q[-1]<nums[right]:
                max_q.pop()
            max_q.append(nums[right])


            while max_q[0] -min_q[0]>limit:
                num=nums[left]
                if max_q[0]==num:
                    max_q.popleft()
                if min_q[0]==num:
                    min_q.popleft()
                left+=1
            maxsize=max(maxsize,right-left+1) 
        return maxsize 