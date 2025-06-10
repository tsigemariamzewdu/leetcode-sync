class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window=set()
        maxi=float("-inf")
        left=0
        if s=="":
            return 0
        for right in range(len(s)):

            
            while s[right] in window:
                window.remove(s[left])
                left+=1
            
            window.add(s[right])
                
            maxi=max(maxi,len(window))
        return maxi


      
        


        