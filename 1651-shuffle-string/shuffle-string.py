class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        result=[None]*len(s)

        for index in range(len(s)):
            finalpos=indices[index]
            char=s[index]

            result[finalpos]=char
        
        return "".join(result)


       