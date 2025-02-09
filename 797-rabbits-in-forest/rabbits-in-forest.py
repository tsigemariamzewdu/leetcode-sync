class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        mydict={}
        count=0
        for i in answers:
            if i==0:
                count+=1
            else:
                if i not in mydict or i==mydict[i]:
                    mydict[i]=0
                    count +=1 +i
                else:
                    mydict[i] += 1
        return count
        