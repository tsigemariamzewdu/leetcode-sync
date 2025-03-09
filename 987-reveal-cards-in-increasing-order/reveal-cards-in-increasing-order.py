from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        res=deque()

        for i in reversed(deck):
            if res:
                res.appendleft(res.pop())
            res.appendleft(i)
        return list(res)

       
        
       
        
            
        