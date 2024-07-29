class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        if len(p)> len(s):
            return []  # because if this is the case we need to return empty list
            #so this is one of the edge cases 
        # since we are finding all the anagrams in a string we need to count the occurence of the letters so i am gonna use a dictionary for this purpose
        pcount={}
        scount={}
        for i in range(len(p)):
            pcount[p[i]]=1+pcount.get(p[i],0)
            scount[s[i]]=1+scount.get(s[i],0)
            # this is another way of counting i have seen it somewhere before but never used before
        newlist=[0] if scount==pcount else []
        # now lets assign the pointers 
        l=0
        for r in range(len(p),len(s)):
            scount[s[r]]=1+scount.get(s[r],0)
            scount[s[l]]-=1
            if scount[s[l]]==0:
                scount.pop(s[l])
            l += 1
            if scount ==pcount:
                newlist.append(l)
        return newlist

        

        