# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        allsums=[]
        def dfs(node):
            if node is None:
                return 0
            s= node.val + dfs(node.left) + dfs(node.right)
            allsums.append(s)
            return s
        totalsum=dfs(root)
        res=0
        for s in allsums:
            res=max(res,s * (totalsum-s))
        return res % ((10**9) + 7 )
