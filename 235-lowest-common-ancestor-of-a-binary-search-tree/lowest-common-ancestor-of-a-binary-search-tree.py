# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca=root

        def binary(root):
            nonlocal lca
            if not root:
                return

            if root:
                if p.val<root.val and q.val<root.val:
                    lca=root.left
                 
                    binary(root.left)
                elif  p.val>root.val and q.val>root.val:
                    lca=root.right
                    binary(root.right)
             
        binary(root)
        return lca
                


        