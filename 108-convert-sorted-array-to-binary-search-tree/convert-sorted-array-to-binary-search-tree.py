# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

      
        def helper(start, end):
            if start > end:
                return None
            if start==end:
                return TreeNode(nums[start])
            # if len(nums)==0:
            #     return None
            # if len(nums)==1:
            #     return TreeNode(nums[0])
            
          
           
            mid=(start+end)//2
            
       
            root=TreeNode(nums[mid])
            root.left=helper(start,mid-1)
            root.right=helper(mid+1,end)

            return root

        return helper(0,len(nums)-1)
       

    
        
        


       
        

        