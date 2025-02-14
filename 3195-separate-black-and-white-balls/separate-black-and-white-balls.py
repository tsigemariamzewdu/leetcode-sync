class Solution:
    def minimumSteps(self, s: str) -> int:
        l=0
        count_ones=0
        swap=0
        while l<len(s):
            if int(s[l])==1:
                count_ones+=1
            else:
                if count_ones>0 and int(s[l])==0:
                    swap+=count_ones
            l+=1
        return swap



        