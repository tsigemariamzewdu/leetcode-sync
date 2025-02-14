class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        summ=0
        l=0
        size=len(cardPoints)-k
        n=0
        answer=0
        total=sum(cardPoints)
        for r in range(len(cardPoints)):
            summ+=cardPoints[r]
            n+=1
            print(summ)
            print(size)

            if n==size:
                answer=max(answer,total-summ)
                summ-=cardPoints[l]
                n-=1
                l+=1
        if answer==0:
            return total
        return answer





        