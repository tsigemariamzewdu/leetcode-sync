class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        i=0
        j=0

        count=0
        while i<len(g) and j<len(s):
            if g[i]<= s[j]:
                count +=1
                i+=1
                j+=1
            elif g[i]>s[j]:
                j+=1
        return count
            

       
        