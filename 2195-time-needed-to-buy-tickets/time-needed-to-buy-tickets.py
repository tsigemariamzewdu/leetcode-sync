from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue=deque(range(len(tickets)))
        ans=0
        while tickets[k]:
            ind=queue.popleft()
            tickets[ind]-=1
            ans +=1
            if tickets[ind]>0:
                queue.append(ind)
        return ans

        