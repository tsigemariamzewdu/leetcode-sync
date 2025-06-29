# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
       
    
        ans=[]
        
        def helper(root,result,realresult):

            if not root:
                return 
            if root:
               
            
                result+= str(root.val)
                if not root.left and not root.right:
                    ans.append(int(result))
                   
              
                helper(root.left,result,realresult)
                helper(root.right,result,realresult)

           
        helper(root,"",0)
        return sum(ans)
        
       