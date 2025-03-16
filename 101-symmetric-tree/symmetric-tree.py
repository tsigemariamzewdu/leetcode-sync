# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        result=[]
       
        sec=[]
        def helper(root):
            if root:
                result.append(root.val)
                helper(root.left)
                helper(root.right)
            if not root:
                result.append(-1)
            
            

        def helper2(root):
            if root:
                sec.append(root.val)
                helper2(root.right)
                helper2(root.left)
            if not root:
                sec.append(-1)
            
        
        helper(root.left)

        helper2(root.right)
      
        return  result==sec
        


        