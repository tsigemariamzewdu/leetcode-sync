# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
            if i%2!=0:
                result.append(res[i][::-1])
            else:
                result.append(res[i])
        return result


        # return res