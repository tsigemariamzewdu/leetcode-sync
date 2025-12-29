class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        mp=defaultdict(list)
        for a in allowed:
            mp[a[:2]].append(a[2])
        memo=set()

        def dfs(row):
            if len(row)==1:
                return True
            if row in memo:
                return False
            c=[]
            def backtrack(i,path):
                if i==len(row)-1:
                    c.append("".join(path))
                    return
                pair= row[i:i+2]
                if pair not in mp:
                    return 
                for ch in mp[pair]:
                    backtrack(i+1,path+[ch])
            backtrack(0,[])
            for next_row in c:
                if dfs(next_row):
                    return True
            memo.add(row)
            return False
        return dfs(bottom)
        