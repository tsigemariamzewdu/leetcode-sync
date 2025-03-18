# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def level_rec(root: Optional[TreeNode], level: int, res: List[List[TreeNode]]):
           
            if not root:
                return
            
           
            if len(res) <= level:
                res.append([])
            
           
            res[level].append(root)
            
           
            level_rec(root.left, level + 1, res)
            level_rec(root.right, level + 1, res)
        
      
        res = []
        level_rec(root, 0, res)
        
      
        for level in range(len(res)):
            if level % 2 != 0: 
                nodes = res[level]
                l, r = 0, len(nodes) - 1
                while l < r:
                   
                    nodes[l].val, nodes[r].val = nodes[r].val, nodes[l].val
                    l += 1
                    r -= 1
        
        return root