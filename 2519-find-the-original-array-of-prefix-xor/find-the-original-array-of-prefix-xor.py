class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ini=[pref[0]]

        for i in range(1,len(pref)):
            newpref=pref[i-1]^pref[i]
            ini.append(newpref)
        return ini