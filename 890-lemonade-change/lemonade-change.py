class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5=0
        count10=0

        for i in range(len(bills)):
            if bills[i]==5:
                count5+=1
            elif bills[i]==10:
                count10+=1
                if count5<1:
                    return False
                else:
                    count5-=1
            elif bills[i]==20:
                if count5<1:
                    return False
                if (count10<1 and count5<3):
                    return False
                elif count10<1 and count5>3:
                
                    count5-=3
                else:
                    count10-=1
                    count5-=1

        return True
        