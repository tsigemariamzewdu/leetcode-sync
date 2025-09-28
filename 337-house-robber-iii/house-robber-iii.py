# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo={}

        def dp(n):
            if not n:
                return 0
            if  n not in memo:
                rob=n.val
                left=n.left
                right=n.right

                if left:
                    if left.left:
                        rob+=dp(left.left)
                    if left.right:
                        rob+=dp(left.right)
                if right:
                    if right.left:
                        rob+=dp(right.left)
                    if right.right:
                        rob+=dp(right.right)
                skip=dp(left)+dp(right)
                memo[n]=max(skip,rob)
               
            
            return memo[n]
        return dp(root)
        