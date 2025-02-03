class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        z_l=[]
        o_l=[]

        
        winnercount=Counter(match[0] for match in matches)
        loosercount=Counter(match[1]for match in matches)
        for i in winnercount:
            if i not in loosercount:
                z_l.append(i)
        for j in loosercount:
            if loosercount[j]==1:
                o_l.append(j)
        
        z_l.sort()
        o_l.sort()
        return[z_l,o_l]
        



        