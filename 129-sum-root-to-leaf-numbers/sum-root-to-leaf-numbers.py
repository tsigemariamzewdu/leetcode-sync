# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
       
    
        ans=[]
        
        def helper(root,res,realresult):

            if not root:
                return 
            if root:
               
            
                res += str(root.val)
                if not root.left and not root.right:
                    ans.append(int(res))
                   
              
                helper(root.left,res,realresult)
                helper(root.right,res,realresult)

           
        helper(root,"",0)
        return sum(ans)
        
       