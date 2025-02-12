class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l=0
        r=len(skill)-1
        if len(skill)>2:
            team=skill[l]+skill[r]
            teams=[]
            while l<r:
                if skill[l]+skill[r]!=team:
                    return -1
                else:
                    teams.append(skill[l]*skill[r])
                    l+=1
                    r-=1
            return sum(teams)
        else:
            return skill[0]*skill[1]

        
    