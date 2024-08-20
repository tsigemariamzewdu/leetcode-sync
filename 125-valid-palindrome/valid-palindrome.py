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
        left=0
        right=len(newString)-1
        while left <right:
            if newString[left]!=newString[right]:
                return False
            left +=1
            right -=1
        return True
        
        
        