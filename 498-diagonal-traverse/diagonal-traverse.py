class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        lists=defaultdict(list)

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                lists[r+c].append(mat[r][c])
        ans=[]
        
        for i in range(len(lists)):
            if i%2!=0:
                ans.extend(lists[i])
            else:
                lists[i].reverse()
                ans.extend(lists[i])
        return ans

        