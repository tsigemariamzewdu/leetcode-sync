from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(player, l, r):
          
            if l == r:
                if player == 1:
                    return nums[l] 
                else:
                    return -nums[l] 
            if player == 1:
               
                option1 = nums[l] + helper(2, l + 1, r)
                option2 = nums[r] + helper(2, l, r - 1)
                return max(option1, option2)
            else:
               
                option1 = -nums[l] + helper(1, l + 1, r)
                option2 = -nums[r] + helper(1, l, r - 1)
                return min(option1, option2)

       
        score_diff = helper(1, 0, len(nums) - 1)
        return score_diff >= 0
                





        
        
