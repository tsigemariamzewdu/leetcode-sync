# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, numss: List[int]) -> Optional[TreeNode]:

      
        def helper(nums):
            if len(nums)==0:
                return None
            if len(nums)==1:
                return TreeNode(nums[0])
            
          
            n=len(nums)
        
            leftarr=nums[:n//2]
            rightarr=nums[(n//2)+1:]
       
            root=TreeNode(nums[n//2])
            root.left=helper(leftarr)
            root.right=helper(rightarr)

            return root

        return helper(numss)
       

    
        
        


       
        

        