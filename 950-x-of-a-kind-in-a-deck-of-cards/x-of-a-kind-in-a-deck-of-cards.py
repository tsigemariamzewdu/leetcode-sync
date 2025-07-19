class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck)==1:
            return False
        counter=Counter(deck)
        lists=[]
        for i in counter:
            lists.append(counter[i])
        maxi=lists[0]
        for i in lists:
            maxi=math.gcd(maxi,i)
        return maxi!=1