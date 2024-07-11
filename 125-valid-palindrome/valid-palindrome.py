class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newString= ""
        for i in s.lower():
            if i.isalpha() or i.isdigit():
                newString+=i
        reversedString=newString[::-1]
        return newString==reversedString
        
        