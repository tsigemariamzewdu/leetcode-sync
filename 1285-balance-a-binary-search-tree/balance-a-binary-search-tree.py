# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res=[]
        def dfs(root):
            if root:
                dfs(root.left)
                res.append(root.val)
                dfs(root.right)
        dfs(root)
        

        
        def helper(res):
            if len(res)==0:
                return None
            if len(res)==1:
                return TreeNode(res[0])

            mid=len(res)//2

            root=TreeNode(res[mid])
            root.left=helper(res[:mid])
            root.right=helper(res[mid+1:])

            return root
        return helper(res)
    
                