class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels={"a","e","i","o","u"}
        count=0
        for i in s:
            if i in vowels:
                count+=1
        if count==0:
            return False
        else:
            return True
        