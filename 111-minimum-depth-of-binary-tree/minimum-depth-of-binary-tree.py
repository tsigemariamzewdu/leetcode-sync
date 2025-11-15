# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue=deque([])
        queue.append((root,1))
        min_depth=float("inf")

        if not root:
            return 0

        while queue:

            node,lv=queue.popleft()
            if not node:
                return min_depth
            if not node.left and not node.right:
                min_depth=min(min_depth,lv)
            if node.left:
                queue.append((node.left,lv+1))
            if node.right:
                queue.append((node.right,lv+1))
        return min_depth


        