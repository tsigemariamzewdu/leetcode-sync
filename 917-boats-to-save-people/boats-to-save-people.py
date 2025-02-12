class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l=0
        people.sort()
        r=len(people)-1
        numboat=0
        while l<r:
            if people[l]+people[r]>limit:
                numboat+=1
                r-=1
            if people[l]+people[r]<=limit:
                numboat+=1
                l+=1
                r-=1
        if l==r:
            numboat+=1
        return numboat


        