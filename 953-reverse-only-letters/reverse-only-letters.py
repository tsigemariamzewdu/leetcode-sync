class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # i need two pointers to deal with this problem so 
        news=list(s)
        i=0
        j= len(s)-1
        while i <j:
            if news[i].isalpha() and news[j].isalpha():
                news[i],news[j]=news[j],news[i]
                i+=1
                j-=1
            elif  not news[i].isalpha():
                i+=1
            else:
                j-=1
        return ''.join(news)
        