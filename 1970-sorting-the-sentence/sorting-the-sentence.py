class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split() 
        sorted_words =sorted(words, key=lambda x: x[-1])

        res=[]
        for word in sorted_words:
            res.append(word[:-1]) 
        return " ".join(res)

       
        