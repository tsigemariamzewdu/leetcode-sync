# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return 
        if root.val==key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

        # delter function
        def deleter(parent,current):
            if current.val<parent.val:
                
                if current.left:
                    parent.left=current.left
                else:
                    parent.left=current.right
            else:
                if current.right:
                    parent.right=current.right
                else:
                    parent.right=current.left

            

        # inorder pred

        def inpred(parent,current):
            if not current.right:
                x=current.val
                deleter(parent,current)
                return x
            return inpred(current,current.right)
        
        # inorder suc

        def insuc(parent,current):
            if not current.left:
                x=current.val
                deleter(parent,current)
                return x
            return insuc(current,current.left)
            


          
        def helper(parent,current):
            if not current:
                return 
            if current.val==key:
                if current.left:
                    x=inpred(current,current.left)
                    current.val=x
                elif current.right:
                    x=insuc(current,current.right)
                    current.val=x
                else:
                    deleter(parent,current)
            elif key>current.val:
                helper(current,current.right)
            else:
                helper(current,current.left)
           
        helper(None,root)
        return root
        
