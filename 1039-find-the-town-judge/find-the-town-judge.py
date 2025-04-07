class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
      
        mapp = defaultdict(set)
        
       
        trusts = set()

        for a, b in trust:
            mapp[b].add(a)
            trusts.add(a)

        for k in range(1, n + 1):
           
            if len(mapp[k]) == n - 1 and k not in trusts:
                return k
        
        return -1
