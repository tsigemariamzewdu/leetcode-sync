# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def levelrec(root,level,res):
            if not root:
                return
            if len(res)<=level:
                res.append([])
            res[level].append(root.val)

            levelrec(root.left,level+1,res)
            levelrec(root.right,level+1,res)

        res=[]
        levelrec(root,0,res)
        result=[]
        for i in range(len(res)):
            result.append(max(res[i]))
        return result
                
        
        
        