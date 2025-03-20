# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total=0
        def dfs(root):
            nonlocal total
            if root:
                dfs(root.right)
                root.val+=total
                total=root.val
                dfs(root.left)
        dfs(root)
        return root

            
        