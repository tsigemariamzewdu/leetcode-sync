class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans=0
        prev_ones=0
        for b in bank:
            curr_ones=0
            
            for i in range(len(b)):
                if b[i]=="1":
                    curr_ones+=1
            ans += prev_ones * curr_ones
            if curr_ones!=0:
                prev_ones=curr_ones
        return ans

                

        