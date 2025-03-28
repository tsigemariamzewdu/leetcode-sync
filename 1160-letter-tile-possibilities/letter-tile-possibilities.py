class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        path=[]
        ans=[]
        counter=Counter(tiles)
        def backtrack(idx):
            nonlocal counter
            if path[:]  not in ans:
                ans.append(path[:])
            if idx>len(tiles):
                return




            for i in tiles:
                if counter[i]>0:
                    path.append(i)
                    counter[i]-=1
                    backtrack(idx+1)
                    path.pop()
                    counter[i]+=1
                    

            return
        backtrack(0)
        return len(ans)-1


        