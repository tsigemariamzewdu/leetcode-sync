"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(row,col,n):
            flag=True
            for r in range(n):
                for c in range(n):
                    if grid[row+r][col+c]!=grid[row][col]:
                        flag=False
            if flag:
                return Node(grid[row][col],True)
            n=n//2
            topleft=helper(row,col,n)
            topright=helper(row,col+n,n)
            bottomleft=helper(row+n,col,n)
            bottomright=helper(row+n,col+n,n)

            return Node(0,False,topleft,topright,bottomleft,bottomright)
        return helper(0,0,len(grid))