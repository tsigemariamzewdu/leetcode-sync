from collections import deque
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        # 2,3,5,7,11,13,17
        result=deque()
        for i in reversed(deck): # 17,,13,11,7,5,3,2
            if result:
                result.appendleft(result.pop())
            result.appendleft(i) # this right here appends 17 to the left side 
        return list(result)
