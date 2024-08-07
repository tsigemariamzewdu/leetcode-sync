class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        counts=[0]*26
        for c in word:
            counts[ord(c)-ord("a")]+=1
        counts.sort(reverse=True)
        result=0
        unique=0
        for count in counts:
            result += count*(1+unique//8)
            unique +=1
        return result
        