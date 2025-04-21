# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = []
        
        def dfs(node):
            if node is None:
                return
            
            result.append(str(node.val))
            
            if node.left or node.right:
                result.append("(")
                dfs(node.left)
                result.append(")")
                
                if node.right:
                    result.append("(")
                    dfs(node.right)
                    result.append(")")
        
        dfs(root)
        return "".join(result)