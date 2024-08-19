class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split() # this returns a list as we know 
        sorted_words =sorted(words, key=lambda x: x[-1])

        news=[]
        for word in sorted_words:
            news.append(word[:-1]) # since we dont want the number to show up 
        return " ".join(news)

       
        