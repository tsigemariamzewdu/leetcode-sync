# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count=0
       

        def dfs(root):
            nonlocal count
            
            if not root:
                return (0,0)

            
            totalleft,sizeleft=dfs(root.left)
            totalright,sizeright=dfs(root.right)
            total= root.val+ totalleft+totalright
            size=1+sizeleft+sizeright

            if root.val==total//size:
                count+=1
            
            return (total,size)
                
               
               
        dfs(root)
        return count

           
            


        