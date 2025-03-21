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
        

        
        def helper(start,end):
            if start>end:
                return None
            if start==end:
                return TreeNode(res[start])

            mid=(start+end)//2

            root=TreeNode(res[mid])
            root.left=helper(start,mid-1)
            root.right=helper(mid+1,end)

            return root
        return helper(0,len(res)-1)
    
                