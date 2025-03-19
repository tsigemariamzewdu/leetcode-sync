# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def helper(root):
            if not root:
                newnode=TreeNode(val)
                return newnode
            else:
                if val>root.val:
                    root.right=helper(root.right)
                elif val<root.val:
                    root.left=helper(root.left)
            return root
        return helper(root)
       
        
        
        

    