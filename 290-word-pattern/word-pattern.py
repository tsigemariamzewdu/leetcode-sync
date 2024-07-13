class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s1=s.split()
        
        if len(s1)!=len(pattern):
            return False


        pdict = {}
        sdict = {}

        for i in range(len(pattern)):
            if pattern[i] in pdict:
                if pdict[pattern[i]] != s1[i]:
                    return False
            else:
                pdict[pattern[i]] = s1[i]

            if s1[i] in sdict:
                if sdict[s1[i]] != pattern[i]:
                    return False
            else:
                sdict[s1[i]] = pattern[i]

        return True
