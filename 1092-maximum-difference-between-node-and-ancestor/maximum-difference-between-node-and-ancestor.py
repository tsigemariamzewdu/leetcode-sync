# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        diff=[]
        def helper(root,mini,maxi):
           
            if root:

                mini=min(mini,root.val)
                maxi=max(maxi,root.val)
                diff.append(maxi-mini)
                helper(root.left,mini,maxi)
                helper(root.right,mini,maxi)

            return diff
        return max(helper(root,root.val,root.val))
        

        
     

     
        